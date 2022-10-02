from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import DateTimeField
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from app_token_auth.auth import TokenAuthentication
from app_token_auth.models import AuthToken, UserType
from app_token_auth.settings import AtAUTH_settings
from Libraries.functions.types.list_of_strings.main import object_is_list_of_strings
from Libraries.functions.print.main import app_debug_printer


class LoginView(APIView):
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated,)

    def get_context(self):
        return {'request': self.request, 'format': self.format_kwarg, 'view': self}

    def get_token_ttl(self):
        return AtAUTH_settings.TOKEN_TTL

    def get_token_limit_per_user(self):
        return AtAUTH_settings.TOKEN_LIMIT_PER_USER

    def get_user_serializer_class(self):
        return AtAUTH_settings.USER_SERIALIZER

    def get_expiry_datetime_format(self):
        return AtAUTH_settings.EXPIRY_DATETIME_FORMAT

    def format_expiry_datetime(self, expiry):
        datetime_format = self.get_expiry_datetime_format()
        return DateTimeField(format=datetime_format).to_representation(expiry)  # type: ignore

    def get_post_response_data(self, request, token, instance):
        UserSerializer = self.get_user_serializer_class()
        # print({"UserSerializer": UserSerializer})

        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        print({"request": request})
        if hasattr(request, "extra_info") and request.extra_info is not None:
            extra_info = request.extra_info
            if type(extra_info) is dict:
                for key in extra_info.keys():
                    value = extra_info[key]
                    _list_of_strings = object_is_list_of_strings(value)
                    # app_debug_printer(
                    #     __file__, description="_object_is_list_of_strings", output=_list_of_strings
                    # )
                    if not _list_of_strings:
                        raise Exception(f"'extra_info' value with key '{key}' must be of type list[str], {type(value)} given")
                data["extra_info"] = extra_info
            else:
                raise Exception(f"'extra_info' must be of type dict[str, list[str]], {type(extra_info)} given")

        if UserSerializer is not None:
            # print({"request.user": request.user, "context": self.get_context()})
            data["user"] = UserSerializer(
                request.user,  # type: ignore
                context=self.get_context()
            ).data
        return data

    def post(self, request, account_type: UserType, format=None):
        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = request.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                return Response(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=status.HTTP_403_FORBIDDEN
                )
        token_ttl = self.get_token_ttl()
        instance, token = AuthToken.objects.create(
            account_type, request.user, token_ttl)  # type: ignore
        user_logged_in.send(sender=request.user.__class__,
                            request=request, user=request.user)
        data = self.get_post_response_data(request, token, instance)
        return Response(data)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LogoutAllView(APIView):
    '''
    Log the user out of all sessions
    I.E. deletes all auth tokens for the user
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token_set.all().delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return Response(None, status=status.HTTP_204_NO_CONTENT)
