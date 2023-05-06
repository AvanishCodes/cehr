# doctor/views/association.py
from rest_framework import generics

from django_filters import rest_framework as filters

from ..models import Association
from ..serializers import AssociationSerializer
from ..pagination import DefaultPagination
from ..filters import AssociationFilter


class AssociationListCreate(generics.ListCreateAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    pagination_class = DefaultPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AssociationFilter


class AssociationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer


__all__ = (
    AssociationListCreate,
    AssociationDetail
)
