# doctor/filters/doctor.py
from django_filters.rest_framework import FilterSet, CharFilter

from ..models import Doctor


class DoctorFilter(FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    middle_name = CharFilter(field_name='middle_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    reg_no = CharFilter(field_name='reg_no', lookup_expr='icontains')
    user__email = CharFilter(field_name='user__email', lookup_expr='icontains')
    specialization__name = CharFilter(field_name='specialization__name', lookup_expr='icontains')
    highest_qualification__name = CharFilter(field_name='highest_qualification__name', lookup_expr='icontains')
    
    class Meta:
        model = Doctor
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'reg_no',
            'user__email',
            'specialization__name',
            'highest_qualification__name',
        )

__all__ = (
    DoctorFilter,
)
