from rest_framework import serializers


class FormIntegerField(serializers.IntegerField):
    def to_internal_value(self, data):
        # print({"data": data})
        return int(data)
        # return super().to_internal_value(int(data))

    def to_representation(self, value):
        return int(value)

    def to_native(self, value):
        return int(value)