from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from app_token_auth import crypto
from app_token_auth.settings import CONSTANTS, AtAUTH_settings

# from db_models_plus_database_1.models.clients.users.user import UserModel

User = User

class UserType(models.IntegerChoices):
    user = 1, 'User'

class AuthTokenManager(models.Manager):
    def create(self, account_type, user, expiry=AtAUTH_settings.TOKEN_TTL):
        token = crypto.create_token_string()
        digest = crypto.hash_token(token)

        if expiry is not None:
            expiry = timezone.now() + expiry # type: ignore

        if type(user) is not int:
            user = user.id

        instance = super(AuthTokenManager, self).create(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH], digest=digest,
            account_type=account_type, user=user, expiry=expiry)
        return instance, token


class AuthToken(models.Model):

    objects = AuthTokenManager()

    digest = models.CharField(
        max_length=CONSTANTS.DIGEST_LENGTH,
        primary_key=True
    )

    token_key = models.CharField(
        max_length=CONSTANTS.TOKEN_KEY_LENGTH,
        db_index=True
    )

    account_type = models.PositiveSmallIntegerField(
        blank=False, null=True, choices=UserType.choices,
        default=UserType.user
    )

    user = models.PositiveIntegerField(
        null=False, blank=False,
    )

    def getUser(self):
    
        return User.objects.filter(id=self.user)  
            

    created = models.DateTimeField(auto_now_add=True)

    expiry = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s : %s' % (self.digest, self.user)
