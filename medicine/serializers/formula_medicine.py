# medicine/serializers/formula_medicine.py
from rest_framework import serializers

from ..models import Formula


class FormulaMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Formula
        fields = ('id', 'shorthand', 'name', 'type', 'description',)
        read_only_fields = ('id',)

__all__ = (
    FormulaMedicineSerializer,
)
