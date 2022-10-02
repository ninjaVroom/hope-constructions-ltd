from typing import Any
from django.contrib.auth.models import User
from app_token_auth.models import UserType


def current_api_user(context, action=None):
    __current_user = context['request'].user
    if type(__current_user) == User:
        response = UserType.user, __current_user.accountId
        if action is not None:
            action(userType=UserType.user, clientId=__current_user.id)
    else:
        response = None
            
    return response