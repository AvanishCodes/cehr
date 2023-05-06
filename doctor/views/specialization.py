# doctor/views/speciaization.py
from rest_framework import generics

from ..models import Specialization

from ..serializers import SpecializationSerializer


class SpecializationListCreate(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SpecializationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
