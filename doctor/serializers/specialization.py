# doctor/serializers/specialization.py
from rest_framework import serializers

from ..models import Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('shorthand', 'name', 'description')