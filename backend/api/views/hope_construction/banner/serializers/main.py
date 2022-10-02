from rest_framework import serializers
from api.views.hope_construction.files.serializers.main import FilesHCSerializer
from hope_construction.models.banner.main import BannerHCModel


class BannerHCSerializer(serializers.ModelSerializer):
    banner = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(BannerHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = BannerHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields