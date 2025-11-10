from django.urls import path
from .views import quality_page

urlpatterns = [
    path('', quality_page, name='quality-page'),
]
