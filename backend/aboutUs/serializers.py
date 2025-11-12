from rest_framework import serializers
from .models import Page, Element, Product, Files
from home.serializers import AbsoluteImageUrlField


# ✅ Product
class ProductSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "image"]


# ✅ Files
class FilesSerializer(serializers.ModelSerializer):
    file = AbsoluteImageUrlField()

    class Meta:
        model = Files
        fields = ["id", "file"]


# ✅ Element
class ElementSerializer(serializers.ModelSerializer):
    photo = AbsoluteImageUrlField()
    products = ProductSerializer(many=True, read_only=True)
    files = FilesSerializer(many=True, read_only=True)

    class Meta:
        model = Element
        fields = [
            "id",
            "type",
            "photo",
            "title",
            "description",
            "is_active",
            "products",
            "files",
        ]


# ✅ Page
class PageSerializer(serializers.ModelSerializer):
    elements = ElementSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ["id", "name", "slug", "elements"]
