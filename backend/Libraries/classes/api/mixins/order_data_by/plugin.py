from django.db.models.query import QuerySet


def orderByPlugin(queryset: QuerySet, field: str | bool):
    if field == False:
        return queryset
    return queryset.order_by(field)
