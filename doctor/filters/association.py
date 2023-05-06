
from ..models import Association
from django_filters.rest_framework import FilterSet, CharFilter


class AssociationFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    association_type = CharFilter(field_name='association_type', lookup_expr='exact')
    
    class Meta:
        model = Association
        fields = [
            'name',
            'association_type',
        ]


__all__ = (
    AssociationFilter,
)
