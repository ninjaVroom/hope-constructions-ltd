from rest_framework import serializers
from hope_construction.models.services.main import ServiceHCModel
from api.views.hope_construction.files.serializers.main import FilesHCSerializer


class ServiceHCSerializer(serializers.ModelSerializer):
    image = FilesHCSerializer()
    icon = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(ServiceHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = ServiceHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields