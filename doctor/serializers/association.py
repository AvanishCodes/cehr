# doctor/serializers/association.py
from rest_framework import serializers

from ..models import Association


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = [
            'id',
            'name',
            'type',
            'description',
        ]


__all__ = (
    AssociationSerializer,
)
