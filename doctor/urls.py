from django.urls import path
from .views import (
    AssociationListCreate,
    AssociationDetail,
    SpecializationListCreate,
    SpecializationDetail,
    QualificationListCreate,
    QualificationDetail,
    DoctorListCreate,
    DoctorDetail,
)


urlpatterns = [
    path('associations/', AssociationListCreate.as_view()),
    path('associations/<int:pk>/', AssociationDetail.as_view()),

    path('specializations/', SpecializationListCreate.as_view()),
    path('specializations/<int:pk>/', SpecializationDetail.as_view()),

    path('qualifications/', QualificationListCreate.as_view()),
    path('qualifications/<int:pk>/', QualificationDetail.as_view()),

    path('doctors/', DoctorListCreate.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),
    
]


__all__ = (
    urlpatterns,
)
