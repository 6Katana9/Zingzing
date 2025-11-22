from django.urls import path
from .views import PartnershipRequestCreateView

urlpatterns = [
    path('partnership/', PartnershipRequestCreateView.as_view(), name='partnership_create'),
]
