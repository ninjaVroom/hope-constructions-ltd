from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class DatatableMixin(GenericViewSet):
    """
    Apply this mixin to any view or viewset for datatables
    """
    __request: Request
    __model: models.Model
    __defaultParams: list[str]
    __search: list[str]
    __orderingColumns: dict[str, str] | None = None
    __draw: str
    __queryset: QuerySet
    __recordsTotal: int
    __filteredQueryset: QuerySet
    __filteredQuerysetStartEnd: QuerySet
    __start: int
    __length: int
    __end: int
    __databaseResponse: dict[str, Any]

    def setRequest(self, request: Request):
        self.__request = request

    def getRequest(self):
        return self.__request

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setDefaultParams(self, params: list[str]):
        self.__defaultParams = params

    def getDefaultParams(self):
        return self.__defaultParams

    def setSearchFields(self, search: list[str]):
        _search: list[str] = []
        model = self.getModel()
        for s in search:
            try:
                TYPE = model._meta.get_field(s).get_internal_type() # type: ignore
                # print({"search-field": s, "TYPE": TYPE})

                if 'ForeignKey' != TYPE:
                    if s not in _search:
                        _search.append(s)
            except:
                ### IGNORE NON MODEL FIELDS 
                pass
        self.__search = _search

    def getSearchFields(self):
        return self.__search

    def setOrderingColumns(self, columns: dict[str, str]):
        self.__orderingColumns = columns

    def getOrderingColumns(self):
        return self.__orderingColumns

    def setDraw(self, draw: str):
        self.__draw = draw

    def getDraw(self):
        return self.__draw

    def setQuerySet(self, queryset: QuerySet):
        self.__queryset = queryset

    def getQuerySet(self):
        return self.__queryset

    def setRecordsTotal(self, recordsTotal: int):
        self.__recordsTotal = recordsTotal

    def getRecordsTotal(self):
        return self.__recordsTotal

    def setFilteredQueryset(self, filteredQueryset: QuerySet):
        self.__filteredQueryset = filteredQueryset

    def getFilteredQueryset(self):
        return self.__filteredQueryset

    def setFilteredQuerysetStartEnd(self, filteredQuerysetStartEnd: QuerySet):
        self.__filteredQuerysetStartEnd = filteredQuerysetStartEnd

    def getFilteredQuerysetStartEnd(self):
        return self.__filteredQuerysetStartEnd

    def setStart(self, start: int):
        self.__start = start

    def getStart(self):
        return self.__start

    def setLength(self, length: int):
        self.__length = length

    def getLength(self):
        return self.__length

    def setEnd(self, end: int):
        self.__end = end

    def getEnd(self):
        return self.__end

    def setDatatableResponse(self, databaseResponse: dict[str, Any]):
        self.__databaseResponse = databaseResponse

    def getDatatableResponse(self):
        return self.__databaseResponse

    @action(methods=['get'], detail=False)
    def dataTable(self, model, querySet: QuerySet, request: Request):
        self.setRequest(request)
        self.setQuerySet(querySet)
        self.setModel(model)

        filterset_fields = self.getModel().MetaDb.fields  # type: ignore

        _orderingColumn = self.getOrderingColumns()
        # print("_orderingColumn", self.getOrderingColumns())

        if _orderingColumn == None:
            orderingColumn: dict[str, str] = {}
            orderingColumn['0'] = filterset_fields[0]
            self.setOrderingColumns(orderingColumn)
        else:
            orderingColumn = _orderingColumn

        searchFields: list[str] = []
        for item in filterset_fields:
            searchFields.append(item)
        self.setSearchFields(searchFields)

        requestQueryParams = request.query_params

        dpsExist = False
        dpsFilterValues = {}
        defaultParams = self.getDefaultParams()
        for param in defaultParams:
            if (param in requestQueryParams.keys()):
                dpsExist = True
                dpsFilterValues[param] = requestQueryParams[param]
            else:
                dpsExist = False

        if dpsExist:
            defaultParamsQuerySet = querySet.filter(**dpsFilterValues)
            self.setQuerySet(defaultParamsQuerySet)

        self.datatableResponse()

    @action(methods=['get'], detail=False)
    def dataTable_none_model(self, datas: list, request: Request):
        self.setRequest(request)

        requestQueryParams = request.query_params

        self.datatableResponse_none_model(datas)

    def filter_for_datatable(self, queryset: QuerySet):
        request: Request = self.getRequest()

        draw = request.query_params.get('draw')
        draw = "-" if draw == None else str(draw)
        self.setDraw(draw)

        try:
            start = request.query_params.get('start')
            start = 0 if start == None else int(start)
        except ValueError:
            start = 0
        self.setStart(start)

        try:
            length = request.query_params.get('length')
            length = 10 if length == None else int(length)
        except ValueError:
            length = 10
        self.setLength(length)

        end = length + start
        self.setEnd(end)

        # filtering
        search_query = request.query_params.get('search[value]')
        if search_query:
            query = Q()

            # print({"self.getSearchFields()": self.getSearchFields()})
            for field in self.getSearchFields():

                try:
                    self.getModel()._meta.get_field(field) # type: ignore
                except:
                    continue

                lookup = "{}__icontains".format(field)
                query |= Q(**{lookup: search_query})
                # query &= Q(**{lookup: search_query})

            queryset = queryset.filter(query)

        # ordering
        ordering_column = request.query_params.get('order[0][column]')
        ordering_column = '0' if ordering_column == None else ordering_column

        ordering_direction = request.query_params.get('order[0][dir]')
        ordering = None

        orderingColumns = self.getOrderingColumns()
        orderingColumns = orderingColumns if orderingColumns != None else {}
        # print({"orderingColumns": orderingColumns, "ordering_column": ordering_column})

        ordering = orderingColumns[str(ordering_column)]
        # print({"ordering": ordering})
        if ordering and ordering_direction == 'desc':
            ordering = f"-{ordering}"
        if ordering:
            # print({"ordering": ordering})
            queryset = queryset.order_by(ordering)

        self.setFilteredQueryset(queryset)
        return queryset

    def datatableResponse(self, ):
        queryset = self.filter_queryset(self.getQuerySet())
        # print({"queryset": queryset})

        recordsTotal = queryset.count()
        recordsTotal = int(recordsTotal)
        self.setRecordsTotal(recordsTotal)

        filtered_queryset = self.filter_for_datatable(queryset)

        start = self.getStart()
        end = self.getEnd()

        # print({"start":start, "end":end,})

        filtered_queryset_start_end = filtered_queryset[start:end]
        self.setFilteredQuerysetStartEnd(filtered_queryset_start_end)
        serializer = self.get_serializer(
            filtered_queryset_start_end, many=True)

        draw = self.getDraw()
        response = {
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': filtered_queryset.count(),
            'datatable_plugin': True,
            'data': serializer.data
        }
        self.setDatatableResponse(response)
        return Response(response)

    def filter_for_datatable_none_model(self, datas: list):
        request: Request = self.getRequest()

        draw = request.query_params.get('draw')
        draw = "-" if draw == None else str(draw)
        self.setDraw(draw)

        try:
            start = request.query_params.get('start')
            start = 0 if start == None else int(start)
        except ValueError:
            start = 0
        self.setStart(start)

        try:
            length = request.query_params.get('length')
            length = 10 if length == None else int(length)
        except ValueError:
            length = 10
        self.setLength(length)

        end = length + start
        self.setEnd(end)

        return datas

    def datatableResponse_none_model(self, datas: list):
        # print({"datas":datas, "datas":len(datas),})

        recordsTotal = len(datas)
        recordsTotal = int(recordsTotal)
        self.setRecordsTotal(recordsTotal)

        filtered_queryset = self.filter_for_datatable_none_model(datas)
        # print({"filtered_queryset":len(filtered_queryset),})

        start = self.getStart()
        end = self.getEnd()

        # print({"start":start, "end":end,})

        filtered_queryset_start_end = filtered_queryset[start:end]
        # print({"filtered_queryset_start_end":len(filtered_queryset_start_end), "end":end,})
        # self.setFilteredQuerysetStartEnd(filtered_queryset_start_end)
        serializer = self.get_serializer(
            filtered_queryset_start_end, many=True)

        draw = self.getDraw()
        response = {
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': len(filtered_queryset),
            'datatable_plugin': True,
            'data': serializer.data
        }
        self.setDatatableResponse(response)
        return Response(response)
