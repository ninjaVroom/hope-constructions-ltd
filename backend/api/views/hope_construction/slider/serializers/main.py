from rest_framework import serializers
from hope_construction.models.slider.main import SliderHCModel
from api.views.hope_construction.files.serializers.main import FilesHCSerializer


class SliderHCSerializer(serializers.ModelSerializer):
    image = FilesHCSerializer()
    def to_representation(self, instance):
        instance = super(SliderHCSerializer,
                     self).to_representation(instance)
        return instance

    class Meta:
        model = SliderHCModel
        fields = model.MetaDb.fields
        # read_only_fields = fields