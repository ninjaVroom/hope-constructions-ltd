from rest_framework import serializers
from hope_construction.models.contact_info.main import ContactInfoHCModel
from backend.settings import MEDIA_URL


class ContactInfoHCSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        instance = super(ContactInfoHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = ContactInfoHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields