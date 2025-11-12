from rest_framework import serializers
from .models import (
    HeroSection, SecondSection, SecondSectionSmallCard,
    ThirdSection, ThirdSectionBigCard, FourthSectionGrowTogether
)
from home.serializers import AbsoluteImageUrlField


# ✅ Hero Section
class HeroSectionSerializer(serializers.ModelSerializer):
    leftSideImage = AbsoluteImageUrlField()
    rightSideImage1 = AbsoluteImageUrlField()
    rightSideImage2 = AbsoluteImageUrlField()
    rightSideImage3 = AbsoluteImageUrlField()

    class Meta:
        model = HeroSection
        fields = "__all__"


# ✅ Second Section Small Card
class SecondSectionSmallCardSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = SecondSectionSmallCard
        fields = "__all__"


# ✅ Second Section
class SecondSectionSerializer(serializers.ModelSerializer):
    cards = SecondSectionSmallCardSerializer(many=True)

    class Meta:
        model = SecondSection
        fields = ("cards",)


# ✅ Third Section Big Card
class ThirdSectionBigCardSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = ThirdSectionBigCard
        fields = "__all__"


# ✅ Third Section
class ThirdSectionSerializer(serializers.ModelSerializer):
    bigCard = ThirdSectionBigCardSerializer(many=True)

    class Meta:
        model = ThirdSection
        fields = ("bigCard",)


# ✅ Fourth Section Grow Together
class FourthSectionGrowTogetherSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = FourthSectionGrowTogether
        fields = "__all__"
