# medicine/serializers/formula_medicine.py
from rest_framework import serializers

from ..models import FormulaMedicine


class FormulaMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormulaMedicine
        fields = ('id', 'shorthand', 'name', 'type', 'description',)
        read_only_fields = ('id',)

__all__ = (
    FormulaMedicineSerializer,
)
