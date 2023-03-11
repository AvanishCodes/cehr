# doctor/filters/qualification.py
from django_filters.rest_framework import FilterSet, CharFilter

from ..models import Qualification, Specialization


class QualificationFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    qualification_type = CharFilter(field_name='qualification_type', lookup_expr='icontains')
    specialization = CharFilter(
        field_name='specialization',
        lookup_expr='icontains',
        method='filter_specialization',
    )

    class Meta:
        model = Qualification
        fields = ('name', 'qualification_type',)