from rest_framework import serializers
from .models import NewsHeroSection, NewsSecondSection, NewsSecondBlock
from home.serializers import AbsoluteImageUrlField


# ✅ Hero section
class NewsHeroSectionSerializer(serializers.ModelSerializer):
    leftSideImage1 = AbsoluteImageUrlField()
    leftSideImage2 = AbsoluteImageUrlField()
    leftSideImage3 = AbsoluteImageUrlField()
    rightSideImage = AbsoluteImageUrlField()

    class Meta:
        model = NewsHeroSection
        fields = "__all__"


# ✅ Second section blocks
class NewsSecondBlockSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = NewsSecondBlock
        fields = "__all__"


# ✅ Second section
class NewsSecondSectionSerializer(serializers.ModelSerializer):
    firstBlock = NewsSecondBlockSerializer()
    secondBlock = NewsSecondBlockSerializer()
    thirdBlock = NewsSecondBlockSerializer()

    class Meta:
        model = NewsSecondSection
        fields = ("firstBlock", "secondBlock", "thirdBlock")
