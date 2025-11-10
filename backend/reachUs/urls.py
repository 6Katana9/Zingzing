from django.urls import path
from .views import reachus_page

urlpatterns = [
    path('', reachus_page, name='reachus-page'),
]
