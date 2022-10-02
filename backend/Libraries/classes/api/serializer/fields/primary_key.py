from rest_framework import serializers


class FormPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        # print({"data": data})
        return int(data)

    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)
        return int(value.pk)

    def to_native(self, value):
        return int(value)