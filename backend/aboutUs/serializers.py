from rest_framework import serializers
from .models import HeroSection, SecondSection, CountryItem, DropsItem, ThirdSection, ThirdBlock
from home.serializers import AbsoluteImageUrlField


# ✅ Hero Section
class HeroSectionSerializer(serializers.ModelSerializer):
    leftSideImage1 = AbsoluteImageUrlField()
    leftSideImage2 = AbsoluteImageUrlField()
    leftSideImage3 = AbsoluteImageUrlField()
    rightSideImage = AbsoluteImageUrlField()

    class Meta:
        model = HeroSection
        fields = "__all__"


# ✅ CountryItem (для SecondSection.list)
class CountryItemSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = CountryItem
        fields = ["id", "image", "innerTitle", "text", "order"]


# ✅ DropsItem (для SecondSection.dropsList)
class DropsItemSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = DropsItem
        fields = ["id", "image", "dropsTitle", "dropsText", "order"]


# ✅ SecondSection
class SecondSectionSerializer(serializers.ModelSerializer):
    list = CountryItemSerializer(many=True, read_only=True)
    dropsList = DropsItemSerializer(many=True, read_only=True)

    class Meta:
        model = SecondSection
        fields = ["mainTitle", "mainTitleSpan", "list", "dropsList"]


# ✅ ThirdBlock (для ThirdSection.blocks)
class ThirdBlockSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = ThirdBlock
        fields = ["id", "title", "titleSpan", "text", "image", "order"]


# ✅ ThirdSection
class ThirdSectionSerializer(serializers.ModelSerializer):
    blocks = ThirdBlockSerializer(many=True, read_only=True)

    class Meta:
        model = ThirdSection
        fields = ["blocks"]
