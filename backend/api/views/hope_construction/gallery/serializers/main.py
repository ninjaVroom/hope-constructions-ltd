from rest_framework import serializers
from api.views.hope_construction.files.serializers.main import FilesHCSerializer
from hope_construction.models.gallery.main import GalleryHCModel


class GalleryHCSerializer(serializers.ModelSerializer):
    attachment = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(GalleryHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = GalleryHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields