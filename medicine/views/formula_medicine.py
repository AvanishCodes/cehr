# medicine/views/formula_medicine.py
from rest_framework import generics

from ..models import FormulaMedicine
from ..serializers import FormulaMedicineSerializer
from ..pagination import DefaultPagination


class FormulaMedicineListCreate(generics.ListCreateAPIView):
    queryset = FormulaMedicine.objects.all()
    serializer_class = FormulaMedicineSerializer
    pagination_class = DefaultPagination


class FormulaMedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormulaMedicine.objects.all()
    serializer_class = FormulaMedicineSerializer