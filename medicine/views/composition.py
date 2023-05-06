# medicine/views/composition.py
from rest_framework import generics

from ..models import MedicineComposition
from ..serializers import MedicineCompositionSerializer
from ..pagination import DefaultPagination


class MedicineCompositionListCreate(generics.ListCreateAPIView):
    queryset = MedicineComposition.objects.all()
    serializer_class = MedicineCompositionSerializer
    pagination_class = DefaultPagination


class MedicineCompositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicineComposition.objects.all()
    serializer_class = MedicineCompositionSerializer


__all__ = (
    MedicineCompositionListCreate,
    MedicineCompositionDetail,
)
