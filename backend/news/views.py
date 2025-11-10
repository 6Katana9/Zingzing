from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NewsHeroSection, NewsSecondSection
from .serializers import NewsHeroSectionSerializer, NewsSecondSectionSerializer

@api_view(['GET'])
def news_page(request):
    hero = NewsHeroSection.objects.first()
    second_section = NewsSecondSection.objects.first()

    return Response({
        "hero": NewsHeroSectionSerializer(hero).data if hero else {},
        "secondSection": NewsSecondSectionSerializer(second_section).data if second_section else {}
    })
