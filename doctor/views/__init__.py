# doctor/views/__init__.py
from .association import AssociationListCreate, AssociationDetail
from .specialization import SpecializationListCreate, SpecializationDetail
from .qualification import QualificationListCreate, QualificationDetail
from .doctor import DoctorListCreate, DoctorDetail


__all__ = (
    AssociationListCreate,
    AssociationDetail,

    SpecializationListCreate,
    SpecializationDetail,

    QualificationListCreate,
    QualificationDetail,

    DoctorListCreate,
    DoctorDetail,
    
)
