# medieine/serializers/molecule.py

from rest_framework import serializers
from ..models import Molecule

class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ('id', 'shorthand', 'name', 'description',)
        read_only_fields = ('id',)