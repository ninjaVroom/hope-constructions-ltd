from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings

class CustomPageNumberPagination(PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    # page_size_query_param = 'limit'
    page_size_query_param = 'length'