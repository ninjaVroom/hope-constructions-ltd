from rest_framework import serializers
from api.views.hope_construction.files.serializers.main import FilesHCSerializer
from hope_construction.models.logo.main import LogoHCModel


class LogoHCSerializer(serializers.ModelSerializer):
    logoLight = FilesHCSerializer()
    logoDark = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(LogoHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = LogoHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields