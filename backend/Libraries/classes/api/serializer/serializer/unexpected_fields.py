from rest_framework.serializers import Serializer


class UnexpectedFields(Serializer):
    def unexpectedFields(self, fieldsDict: dict):
        new_fields = {}
        for field in self.fields:
            for item in fieldsDict:
                if field == item:
                    new_fields[field] = fieldsDict[field]
        return new_fields