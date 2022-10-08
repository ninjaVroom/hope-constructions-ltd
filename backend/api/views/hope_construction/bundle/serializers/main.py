from dataclasses import dataclass
from django.db.models import QuerySet
from rest_framework import serializers
from api.views.hope_construction.logo.serializers.main import LogoHCModel, LogoHCSerializer
from api.views.hope_construction.about.serializers.main import AboutHCModel, AboutHCSerializer
from api.views.hope_construction.banner.serializers.main import BannerHCModel, BannerHCSerializer
from api.views.hope_construction.slider.serializers.main import SliderHCModel, SliderHCSerializer
from api.views.hope_construction.gallery.serializers.main import GalleryHCModel, GalleryHCSerializer
from api.views.hope_construction.services.serializers.main import ServiceHCModel, ServiceHCSerializer
from api.views.hope_construction.contact_info.serializers.main import ContactInfoHCModel, ContactInfoHCSerializer
from api.views.hope_construction.testimonials.serializers.main import TestimonialHCModel, TestimonialHCSerializer
from api.views.hope_construction.center_image.serializers.main import CenterImageHCModel, CenterImageHCSerializer


@dataclass
class BundledSerializerDataclass():
    logo: QuerySet[LogoHCModel]
    about: QuerySet[AboutHCModel]
    banner: QuerySet[BannerHCModel]
    slider: QuerySet[SliderHCModel]
    gallery: QuerySet[GalleryHCModel]
    services: QuerySet[ServiceHCModel]
    centerImage: QuerySet[CenterImageHCModel]
    contactInfo: QuerySet[ContactInfoHCModel]
    testimonials: QuerySet[TestimonialHCModel]


class BundledHCSerializer(serializers.Serializer):

    def to_representation(self, instance):
        # print({"instance": instance})
        logo = instance.logo
        about = instance.about
        banner = instance.banner
        slider = instance.slider
        gallery = instance.gallery
        services = instance.services
        centerImage = instance.centerImage
        contactInfo = instance.contactInfo
        testimonials = instance.testimonials

        instance = super(BundledHCSerializer,
                     self).to_representation(instance)
        # print({"instance": instance})
        instance['logo'] = LogoHCSerializer(instance=logo, many=True).data
        instance['about'] = AboutHCSerializer(instance=about, many=True).data
        instance['banner'] = BannerHCSerializer(instance=banner, many=True).data
        instance['slider'] = SliderHCSerializer(instance=slider, many=True).data
        instance['gallery'] = GalleryHCSerializer(instance=gallery, many=True).data
        instance['services'] = ServiceHCSerializer(instance=services, many=True).data
        instance['centerImage'] = CenterImageHCSerializer(instance=centerImage, many=True).data
        instance['contactInfo'] = ContactInfoHCSerializer(instance=contactInfo, many=True).data
        instance['testimonials'] = TestimonialHCSerializer(instance=testimonials, many=True).data
        return instance