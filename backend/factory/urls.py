from django.urls import path
from .views import factory_page

urlpatterns = [
    path('', factory_page, name='factory-page'),
]
