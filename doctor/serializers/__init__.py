# doctor/serializers/__init__.py
from .association import AssociationSerializer
from .specialization import SpecializationSerializer
from .qualification import QualificationSerializer
from .doctor import DoctorSerializer

__all__ = (
    AssociationSerializer,
    SpecializationSerializer,
    QualificationSerializer,
    DoctorSerializer,
)
