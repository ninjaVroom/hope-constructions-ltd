from django.db.models import Q
from rest_framework import serializers


class MemberOrgTypeSerializerPrimaryKeyField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        memberId = self.context.get('memberId', None)
        queryset = super(MemberOrgTypeSerializerPrimaryKeyField,
                         self).get_queryset()

        if not memberId:
            if not request:
                accountId = 0
            else:
                accountId = request.data.get('memberId', 0)
        else:
            accountId = memberId
        # print({"accountId": accountId})
        if not accountId or not queryset:
            return queryset.all() # type:ignore
        queryset = queryset.filter(Q(Q(memberId=accountId) | Q(memberId=0)))
        print({"queryset": queryset})
