# doctor/serializers/doctor.py
from rest_framework import serializers

from django_filters import rest_framework as filters

from ..models import Doctor
from .specialization import SpecializationSerializer
from .qualification import QualificationSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user__email = serializers.EmailField(source='user.email', read_only=True)
    specialization = SpecializationSerializer(many=True, read_only=True)
    highest_qualification = QualificationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Doctor
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'user__email',
            'reg_no',
            'specialization',
            'highest_qualification',
        )
        depth = 1


__all__ = (
    DoctorSerializer,
)
