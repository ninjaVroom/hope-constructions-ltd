from typing import Any
from rest_framework import serializers
from app_token_auth.models import (
    AuthToken, UserType, User as UserModel
)


class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        self.Meta.model = UserModel
        self.Meta.fields = [
            "id", "username", "email", "first_name", "last_name"
        ]
        return super().to_representation(instance)


    class Meta:
        model = Any
        # fields = UserModel.MetaDb.fields
        fields = []
