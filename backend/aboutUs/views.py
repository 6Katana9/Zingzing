from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, SecondSection, ThirdSection
from .serializers import HeroSectionSerializer, SecondSectionSerializer, ThirdSectionSerializer

@api_view(['GET'])
def about_us_page(request):
    # Получаем hero
    hero = HeroSection.objects.first()
    hero_data = HeroSectionSerializer(hero, context={"request": request}).data if hero else {}

    # Получаем second section
    second_section = SecondSection.objects.first()
    second_data = SecondSectionSerializer(second_section, context={"request": request}).data if second_section else {}

    # Получаем third section
    third_section = ThirdSection.objects.first()
    third_data = ThirdSectionSerializer(third_section, context={"request": request}).data if third_section else {}

    # Формируем ответ
    return Response({
        "hero": hero_data,
        "secondSection": second_data,
        "thirdSection": third_data
    })
