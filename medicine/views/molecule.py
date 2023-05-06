# medicine/views/molecule.py
from rest_framework import generics

# from django_filters import rest_framework as filters

from ..models import Molecule
from ..serializers import MoleculeSerializer
# from ..filters import MoleculeFilter
from ..pagination import DefaultPagination


class MoleculeListCreate(generics.ListCreateAPIView):
    queryset = Molecule.objects.all()
    serializer_class = MoleculeSerializer
    # filter_class = MoleculeFilter
    pagination_class = DefaultPagination
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = MoleculeFilter


class MolecularDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Molecule.objects.all()
    serializer_class = MoleculeSerializer
    # filter_class = MoleculeFilter


__all__ = (
    MoleculeListCreate,
    MolecularDetail,
)