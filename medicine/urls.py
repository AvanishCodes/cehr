# medicine/urls.py

from django.urls import path

from .views import (
    MoleculeListCreate,
    MolecularDetail,
    MarketerListCreate,
    MarketerDetail,
    FormulaMedicineListCreate,
    FormulaMedicineDetail,

    MedicineCompositionListCreate,
    MedicineCompositionDetail,
)

urlpatterns = [
    path('molecules/', MoleculeListCreate.as_view(), name='molecule-list'),
    path('molecules/<int:pk>/', MolecularDetail.as_view(), name='molecule-detail'),

    path('marketers/', MarketerListCreate.as_view(), name='marketer-list'),
    path('marketers/<int:pk>/', MarketerDetail.as_view(), name='marketer-detail'),

    path('formulas/', FormulaMedicineListCreate.as_view(), name='formula-list'),
    path('formulas/<int:pk>/', FormulaMedicineDetail.as_view(), name='formula-detail'),
    
    path('compositions/', MedicineCompositionListCreate.as_view(), name='composition-list'),
    path('compositions/<int:pk>/', MedicineCompositionDetail.as_view(), name='composition-detail'),
    
]