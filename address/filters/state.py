from django_filters.rest_framework import FilterSet, CharFilter

from ..models import State


class StateFilter(FilterSet):
    country__name = CharFilter(field_name='country__name', lookup_expr='icontains')
    country__id = CharFilter(field_name='country__id', lookup_expr='exact')

    class Meta:
        model = State
        fields = (
            'country__name',
            'country__id',
        )


__all__ = (
    'StateFilter',
)
