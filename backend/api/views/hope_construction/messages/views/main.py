from django.db.models import Q
from rest_framework import (permissions, status)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from Libraries.classes.api.mixins.datatables.datatable import DatatableMixin
from Libraries.functions.serializer.response.success import success_response
from api.views.hope_construction.messages.serializers.main import MessageHCSerializer
from hope_construction.models.messages.main import MessageHCModel


class MessageHCViewSet(DatatableMixin, ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]
    model = MessageHCModel
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
        return MessageHCSerializer


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

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().partial_update(request, *args, **kwargs)
        
    def destroy(self, request, *args, **kwargs):
        self.filter_unique_to_user(request)
        return super().destroy(request, *args, **kwargs)
