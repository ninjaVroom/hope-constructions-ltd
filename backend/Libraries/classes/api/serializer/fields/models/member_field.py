from rest_framework import serializers


class MemberSerializerPrimaryKeyField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        clientId = self.context.get('clientId', None)
        queryset = super(MemberSerializerPrimaryKeyField,
                         self).get_queryset()

        if not clientId:
            if not request:
                accountId = 0
            else:
                accountId = request.data.get('clientId', None)
        else:
            accountId = clientId
        print({"accountId": accountId})
        if not accountId or not queryset:
            return []
        return queryset.filter(clientId=accountId)
