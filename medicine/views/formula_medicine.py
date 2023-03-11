# medicine/views/formula_medicine.py
from rest_framework import generics

from ..models import Formula
from ..serializers import FormulaMedicineSerializer
from ..pagination import DefaultPagination


class FormulaMedicineListCreate(generics.ListCreateAPIView):
    queryset = Formula.objects.all()
    serializer_class = FormulaMedicineSerializer
    pagination_class = DefaultPagination


class FormulaMedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formula.objects.all()
    serializer_class = FormulaMedicineSerializer


__all__ = (
    FormulaMedicineListCreate,
    FormulaMedicineDetail,
)
