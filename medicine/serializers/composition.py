# medicine/serializers/composition.py
from rest_framework import serializers

from ..models import MedicineComposition


class MedicineCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineComposition
        fields = (
            'id',
            'formula',
            'molecule',
            'type',
            'quantity',
            'unit',
        )


__all__ = (
    MedicineCompositionSerializer,
)
