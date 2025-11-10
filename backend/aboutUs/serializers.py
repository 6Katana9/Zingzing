from rest_framework import serializers
from .models import Page, Element, Product, Files


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "image"]


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ["id", "file"]


class ElementSerializer(serializers.ModelSerializer):
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


class PageSerializer(serializers.ModelSerializer):
    elements = ElementSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ["id", "name", "slug", "elements"]
