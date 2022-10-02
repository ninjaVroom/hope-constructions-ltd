from django.contrib.auth import login

from rest_framework import (permissions)
from rest_framework.response import Response

from app_token_auth.views import LoginView
from app_token_auth.models import UserType
from api.views.login.serializers.main import UserLoginSerializer


class UserLoginApiView(LoginView):
    permission_classes = [permissions.AllowAny, ] 

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        account = serializer.validated_data['account'] # type: ignore
        # print({"account": account})
        login(request=request, user=account,)

        return super().post(request=request, account_type=UserType.user, format=format)