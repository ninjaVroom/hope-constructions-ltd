from rest_framework import serializers
from django.db.models import Q


class MembersGroupingsMemberCategorySerializerPrimaryKeyField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        clientId = self.context.get('clientId', None)
        queryset = super(MembersGroupingsMemberCategorySerializerPrimaryKeyField,
                         self).get_queryset()

        if not clientId:
            if not request:
                accountId = 0
            else:
                accountId = request.data.get('clientId', None)
        else:
            accountId = clientId
        # print({"accountId": accountId})
        if not accountId or not queryset:
            return None
        qs = queryset.filter(Q(Q(clientId=accountId) | Q(clientId=0)))
        # print({"qs-qs_qs-qs": qs, "request.data.get('clientId')": request.data})
        return qs
