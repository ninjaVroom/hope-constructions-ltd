from django.db.models import Q
from rest_framework import (permissions, status)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from Libraries.classes.api.mixins.datatables.datatable import DatatableMixin
from Libraries.functions.serializer.response.success import success_response
from api.views.hope_construction.bundle.serializers.main import (
    BundledHCSerializer, BundledSerializerDataclass, AboutHCModel, 
    SliderHCModel, GalleryHCModel, ServiceHCModel, ContactInfoHCModel,
    TestimonialHCModel, BannerHCModel, LogoHCModel
) 

class BundledHCViewSet(DatatableMixin, ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]
    logoModel = LogoHCModel
    logoQueryset = logoModel.objects.all().select_related('createdBy', 'updatedBy')
    aboutModel = AboutHCModel
    aboutQueryset = aboutModel.objects.all().select_related('createdBy', 'updatedBy')
    bannerModel = BannerHCModel
    bannerQueryset = bannerModel.objects.all().select_related('createdBy', 'updatedBy')
    sliderModel = SliderHCModel
    sliderQueryset = sliderModel.objects.all().select_related('createdBy', 'updatedBy')
    galleryModel = GalleryHCModel
    galleryQueryset = galleryModel.objects.all().select_related('createdBy', 'updatedBy')
    serviceModel = ServiceHCModel
    serviceQueryset = serviceModel.objects.all().select_related('createdBy', 'updatedBy')
    contactInfoModel = ContactInfoHCModel
    contactInfoQueryset = contactInfoModel.objects.all().select_related('createdBy', 'updatedBy')
    testimonialModel = TestimonialHCModel
    testimonialQueryset = testimonialModel.objects.all().select_related('createdBy', 'updatedBy')
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    filterset_fields = sliderModel.MetaDb.fields
    ordering_fields = filterset_fields # - for highest
    USER_ID = 0

    def filter_unique_to_user(self, request: Request | None):
        # print({"filterset_fields": self.filterset_fields})
        # print({"self.request.user": self.request.user.__dict__})
        # userId = int(self.request.user.id)  # type: ignore
        # self.USER_ID = userId
        # self.queryset = self.queryset.filter(Q(Q(createdBy=userId) | Q(updatedBy=userId)))
        pass

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return BundledHCSerializer


    def retrieve(self, request: Request, pk=None):
        self.filter_unique_to_user(request)
        RES = super().retrieve(request, pk)
        _data = RES.data
        DATA = {} if _data is None else _data

        # print({"DATA": DATA})

        return Response(success_response(
            message="", data=DATA
        ), status=RES.status_code)

    def list(self, request: Request):
        self.filter_unique_to_user(request)
        queryset = BundledSerializerDataclass(
            about=self.aboutQueryset.all(), slider=self.sliderQueryset.all(),
            gallery=self.galleryQueryset.all(), services=self.serviceQueryset.all(),
            contactInfo=self.contactInfoQueryset.all(), testimonials=self.testimonialQueryset.all(),
            banner=self.bannerQueryset.all(), logo=self.logoQueryset.all()
        )
        serializer = self.get_serializer(queryset, many=False)
        DATA = serializer.data

        return Response(success_response(
            message="", data=DATA
        ), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().partial_update(request, *args, **kwargs)

    @action(methods=['patch'], detail=False, url_path='resend/(?P<pk>[^/.]+)$', url_name='resend_message')
    def resend_message(self, request: Request, pk=0):
        newData = {
            'sent': False
        }
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=newData, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # print({"serializer.data": serializer.data})

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        DATA = serializer.data
        headers = self.get_success_headers(DATA)
        DATA['SUCCESS_RESPONSE_MESSAGE'] = "Message Resent"
        return Response(DATA, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().destroy(request, *args, **kwargs)
