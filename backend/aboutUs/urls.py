from django.urls import path
from .views import AboutUsAPIView

urlpatterns = [
    path("pages/<slug:slug>/", AboutUsAPIView.as_view(), name="page-content"),
]
