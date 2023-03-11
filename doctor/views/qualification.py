# doctor/views/qualification.py
from rest_framework import generics

from ..models import Qualification

from ..serializers import QualificationSerializer


class QualificationListCreate(generics.ListCreateAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class QualificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


__all__ = (
    QualificationListCreate,
    QualificationDetail,
)
