from rest_framework import serializers
from hope_construction.models.messages.main import MessageHCModel


class MessageHCSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        instance = super(MessageHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = MessageHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields