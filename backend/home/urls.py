from django.urls import path
from .views import products_home

urlpatterns = [
    path('', products_home, name='home-page'),
]
