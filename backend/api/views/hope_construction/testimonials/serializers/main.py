from rest_framework import serializers
from api.views.hope_construction.files.serializers.main import FilesHCSerializer
from hope_construction.models.testimonials.main import TestimonialHCModel


class TestimonialHCSerializer(serializers.ModelSerializer):
    quoteAuthorImage = FilesHCSerializer()
    image = FilesHCSerializer()
    video = FilesHCSerializer()

    def to_representation(self, instance):
        instance = super(TestimonialHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = TestimonialHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields