from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NewsHeroSection, NewsSecondSection
from .serializers import NewsHeroSectionSerializer, NewsSecondSectionSerializer

@api_view(['GET'])
def news_page(request):
    hero = NewsHeroSection.objects.first()
    second_section = NewsSecondSection.objects.first()

    hero_data = NewsHeroSectionSerializer(hero, context={"request": request}).data if hero else {}
    second_section_data = NewsSecondSectionSerializer(second_section, context={"request": request}).data if second_section else {}

    return Response({
        "hero": hero_data,
        "secondSection": second_section_data
    })
