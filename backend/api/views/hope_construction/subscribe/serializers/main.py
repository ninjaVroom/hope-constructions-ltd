from rest_framework import serializers
from hope_construction.models.subscribers.main import SubscriberHCModel


class SubscriberHCSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        instance = super(SubscriberHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = SubscriberHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields