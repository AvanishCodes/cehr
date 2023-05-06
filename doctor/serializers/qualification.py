# doctor/serializers/qualification.py
from rest_framework import serializers

from ..models import Qualification


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id', 'name', 'qualification_type', 'specialization', 'description')


__all__ = (
    QualificationSerializer,
)
