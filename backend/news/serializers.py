from rest_framework import serializers
from .models import NewsHeroSection, NewsSecondSection, NewsSecondBlock

class NewsHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsHeroSection
        fields = "__all__"

class NewsSecondBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSecondBlock
        fields = "__all__"

class NewsSecondSectionSerializer(serializers.ModelSerializer):
    firstBlock = NewsSecondBlockSerializer()
    secondBlock = NewsSecondBlockSerializer()
    thirdBlock = NewsSecondBlockSerializer()
    
    class Meta:
        model = NewsSecondSection
        fields = ("firstBlock", "secondBlock", "thirdBlock")
