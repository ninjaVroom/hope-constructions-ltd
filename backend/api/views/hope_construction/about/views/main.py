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
from api.views.hope_construction.about.serializers.main import AboutHCSerializer
from hope_construction.models.about.main import AboutHCModel


class AboutHCViewSet(DatatableMixin, ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]
    model = AboutHCModel
    queryset = model.objects.all().select_related('createdBy', 'updatedBy')
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    filterset_fields = model.MetaDb.fields
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
            return AboutHCSerializer


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
        requestQueryParams = request.query_params
        self.filter_unique_to_user(request)

        if ('datatable_plugin' in requestQueryParams.keys()):
            defaultParams = list('userId')
            self.setDefaultParams(defaultParams)

            orderingColumn: dict[str, str] = dict(
                (str(index), newitem) for index, newitem in enumerate(self.model.MetaDb.fields)
            )
            # print({"orderingColumn": orderingColumn})
            self.setOrderingColumns(orderingColumn)

            self.dataTable(self.model, self.get_queryset(), request)
            self.getFilteredQuerysetStartEnd()

            return Response(self.getDatatableResponse())
        else:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                DATA = serializer.data

                return self.get_paginated_response(data=DATA)

            serializer = self.get_serializer(queryset, many=True)
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
