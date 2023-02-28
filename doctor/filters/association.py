
from ..models import Association
from django_filters.rest_framework import FilterSet, CharFilter


class AssociationFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    type = CharFilter(field_name='type', lookup_expr='exact')
    
    class Meta:
        model = Association
        fields = [
            'name',
            'type',
        ]


__all__ = (
    AssociationFilter,
)
