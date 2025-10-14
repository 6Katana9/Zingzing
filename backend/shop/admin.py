from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product

admin.site.register(Product)
admin.site.unregister(Group)