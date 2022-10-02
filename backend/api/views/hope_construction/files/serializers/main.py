from rest_framework import serializers
from hope_construction.models.files.main import FileType, FilesHCModel
from backend.settings import MEDIA_URL


class FilesHCSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        fileType = instance.fileType
        instance = super(FilesHCSerializer,
                     self).to_representation(instance)
        instance['fileType'] = {
            "id": FileType.choices[fileType - 1][0],
            "name": FileType.choices[fileType - 1][1]
        }
        return instance

    class Meta:
        model = FilesHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields