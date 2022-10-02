from rest_framework import serializers
from backend.settings import MEDIA_URL
from hope_construction.models.about.main import AboutHCModel


def setUpClientImage(url: str):
    if ("clients/profile-picture/" in url):
        url = url
    else:
        parts = url.split('/')
        fileName = parts[len(parts) - 1]
        url = f"{MEDIA_URL}/clients/profile-picture/" + fileName
    return url.replace('//', '/').replace(':/', '://')


class AboutHCSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        instance = super(AboutHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = AboutHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields