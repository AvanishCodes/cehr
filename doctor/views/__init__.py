# doctor/views/__init__.py
from .association import AssociationListCreate, AssociationDetail
from .specialization import SpecializationListCreate, SpecializationDetail

__all__ = (
    AssociationListCreate,
    AssociationDetail,

    SpecializationListCreate,
    SpecializationDetail,

    
)
