# doctor/views/doctor.py
from rest_framework import generics

from django_filters import rest_framework as filters

from ..models import Doctor
from ..serializers import DoctorSerializer
from ..filters import DoctorFilter
from ..pagination import DefaultPagination
from ..filters import DoctorFilter


class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_class = DoctorFilter
    pagination_class = DefaultPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DoctorFilter
    
    

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_class = DoctorFilter
