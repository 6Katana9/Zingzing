from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, SecondSection, ThirdSection, FourthSectionGrowTogether
from .serializers import (
    HeroSectionSerializer,
    SecondSectionSmallCardSerializer,
    ThirdSectionSerializer,
    FourthSectionGrowTogetherSerializer
)

@api_view(['GET'])
def products_page(request):
    # Получаем объекты секций
    hero = HeroSection.objects.first()
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    fourth_section = FourthSectionGrowTogether.objects.first()

    # Сериализация hero
    hero_data = HeroSectionSerializer(hero, context={"request": request}).data if hero else {}

    # Сериализация карточек второй секции
    if second_section:
        cards = second_section.cards.all()
        second_data = {
            "cards": SecondSectionSmallCardSerializer(cards, many=True, context={"request": request}).data
        }
    else:
        second_data = {"cards": []}

    # Сериализация остальных секций
    third_data = ThirdSectionSerializer(third_section, context={"request": request}).data if third_section else {}
    fourth_data = FourthSectionGrowTogetherSerializer(fourth_section, context={"request": request}).data if fourth_section else {}

    # Финальный ответ с точной структурой JSON
    return Response({
        "hero": hero_data,
        "secondSectionSmallCard": second_data,
        "thirdSectionBigCards": third_data,
        "fourthSectionGrowTogether": fourth_data
    })
