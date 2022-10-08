from rest_framework import serializers
from api.views.hope_construction.files.serializers.main import FilesHCSerializer
from hope_construction.models.center_image.main import CenterImageHCModel


class CenterImageHCSerializer(serializers.ModelSerializer):
    centerImage = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(CenterImageHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = CenterImageHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields