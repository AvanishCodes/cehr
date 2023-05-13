from django_filters.rest_framework import FilterSet, CharFilter

from ..models import City


class CityFilter(FilterSet):
    country__name = CharFilter(field_name='country__name', lookup_expr='icontains')
    country__id = CharFilter(field_name='country__id', lookup_expr='exact')

    state__name = CharFilter(field_name='state__name', lookup_expr='icontains')
    state__id = CharFilter(field_name='state__id', lookup_expr='exact')

    class Meta:
        model = City
        fields = (
            'country__name',
            'country__id',
            'state__name',
            'state__id',
        )


__all__ = (
    'CityFilter',
)
