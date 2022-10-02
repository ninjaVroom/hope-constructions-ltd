try:
    from hmac import compare_digest  # type: ignore
except ImportError:
    def compare_digest(a, b):
        return a == b

import binascii

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header,
)

from app_token_auth.crypto import hash_token
from app_token_auth.models import AuthToken
from app_token_auth.settings import CONSTANTS, AtAUTH_settings
from app_token_auth.signals import token_expired


def getAuthClient(request):
    users = request.auth.getUser()  # type: ignore
    clientId = 0
    for user in users:
        if hasattr(user, 'accountId'):
            clientId = user.accountId
        if hasattr(user, 'clientId'):
            clientId = user.clientId
    return clientId


class TokenAuthentication(BaseAuthentication):
    '''
    This authentication scheme uses Knox AuthTokens for authentication.

    Similar to DRF's TokenAuthentication, it overrides a large amount of that
    authentication scheme to cope with the fact that Tokens are not stored
    in plaintext in the database

    If successful
    - `request.user` will be a django `User` instance
    - `request.auth` will be an `AuthToken` instance
    '''
    model = AuthToken

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        prefix = AtAUTH_settings.AUTH_HEADER_PREFIX.encode()  # type: ignore

        if not auth:
            return None
        if auth[0].lower() != prefix.lower():
            # Authorization header is possibly for another backend
            return None
        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. '
                    'Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        user, auth_token = self.authenticate_credentials(auth[1])
        return (user, auth_token)

    def authenticate_credentials(self, token):
        '''
        Due to the random nature of hashing a value, this must inspect
        each auth_token individually to find the correct one.

        Tokens that have expired will be deleted and skipped
        '''
        msg = _('Invalid token.')
        token = token.decode("utf-8")
        for auth_token in AuthToken.objects.filter(
                token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH]):
            if self._cleanup_token(auth_token):
                continue

            try:
                digest = hash_token(token)
            except (TypeError, binascii.Error):
                raise exceptions.AuthenticationFailed(msg)
            if compare_digest(digest, auth_token.digest):
                if AtAUTH_settings.AUTO_REFRESH and auth_token.expiry:
                    self.renew_token(auth_token)
                return self.validate_user(auth_token)
        raise exceptions.AuthenticationFailed(msg)

    def renew_token(self, auth_token):
        current_expiry = auth_token.expiry
        new_expiry = timezone.now() + AtAUTH_settings.TOKEN_TTL  # type: ignore
        auth_token.expiry = new_expiry
        # Throttle refreshing of token to avoid db writes
        delta = (new_expiry - current_expiry).total_seconds()
        if delta > AtAUTH_settings.MIN_REFRESH_INTERVAL:
            auth_token.save(update_fields=('expiry',))

    def validate_user(self, auth_token):
        # if not auth_token.user.is_active:
        #     raise exceptions.AuthenticationFailed(
        #         _('User inactive or deleted.'))
        # return (auth_token.user, auth_token)
        return (auth_token.getUser()[0], auth_token)

    def authenticate_header(self, request):
        return AtAUTH_settings.AUTH_HEADER_PREFIX

    def _cleanup_token(self, auth_token):
        # print({"auth_token": auth_token})
        # print({"auth_token.getUser": auth_token.getUser()})
        for other_token in [auth_token]:
            if other_token.digest != auth_token.digest and other_token.expiry:
                if other_token.expiry < timezone.now():
                    other_token.delete()
                    username = other_token.getUser().get_username()
                    token_expired.send(sender=self.__class__,
                                       username=username, source="other_token")
        # print({"auth_token.expiry": auth_token.expiry.strftime('%Y-%m-%d')})
        # print({"timezone.now()": timezone.now().strftime('%Y-%m-%d')})
        if auth_token.expiry is not None:
            if auth_token.expiry < timezone.now():
                # print({"auth_token.user": auth_token.getUser()})
                if auth_token.getUser().exists():
                    username = auth_token.getUser().first().get_username()
                else:
                    username = "user"
                auth_token.delete()
                token_expired.send(sender=self.__class__,
                                   username=username, source="auth_token")
                return True
        return False
