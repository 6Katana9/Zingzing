from rest_framework import serializers
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSection, QualityThirdSectionDrop,
    QualityFourthSectionBlock
)
from home.serializers import AbsoluteImageUrlField


# ✅ Hero section
class QualityHeroSectionSerializer(serializers.ModelSerializer):
    leftSideImage1 = AbsoluteImageUrlField()
    leftSideImage2 = AbsoluteImageUrlField()
    leftSideImage3 = AbsoluteImageUrlField()
    rightSideImage = AbsoluteImageUrlField()

    class Meta:
        model = QualityHeroSection
        fields = "__all__"


# ✅ Second section
class QualitySecondSectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = QualitySecondSection
        fields = "__all__"


# ✅ Third section drops
class QualityThirdSectionDropSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = QualityThirdSectionDrop
        fields = "__all__"


# ✅ Third section
class QualityThirdSectionSerializer(serializers.ModelSerializer):
    dropsList = QualityThirdSectionDropSerializer(many=True)

    class Meta:
        model = QualityThirdSection
        fields = ("dropsList",)


# ✅ Fourth section blocks
class QualityFourthSectionBlockSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = QualityFourthSectionBlock
        fields = "__all__"
