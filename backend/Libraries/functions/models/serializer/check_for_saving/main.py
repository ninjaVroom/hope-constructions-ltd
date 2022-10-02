from typing import Any
from rest_framework import serializers
from django.db.models.query import QuerySet


def serializer__check_model_validity_for_saving(instance: Any = ..., field: str = ..., fieldValue=..., querySet: QuerySet = ...):
    if instance is None:
        if fieldValue is None:
            raise serializers.ValidationError(
                detail={f"{field}": "This field is required."})
        else:
            fieldValue = int(fieldValue)
            if type(fieldValue) is not int:
                raise serializers.ValidationError(
                    detail={f"{field}": "A valid integer is required."})
            else:
                __field = querySet
                if __field.exists():
                    return __field.first()
                else:
                    raise serializers.ValidationError(
                        detail={f"{field}": "Object not found."})
    else:
        if fieldValue is None:
            return instance.field
        else:
            fieldValue = int(fieldValue)
            if type(fieldValue) is not int:
                raise serializers.ValidationError(
                    detail={f"{field}": "A valid integer is required."})
            else:
                __field = querySet
                if __field.exists():
                    return __field.first()
                else:
                    raise serializers.ValidationError(
                        detail={f"{field}": "Object not found."})
