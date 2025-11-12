from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ReachUsHeroSection, ReachUsSecondSection
from .serializers import ReachUsHeroSectionSerializer, ReachUsSecondSectionSerializer

@api_view(['GET'])
def reachus_page(request):
    hero = ReachUsHeroSection.objects.first()
    second_section = ReachUsSecondSection.objects.first()

    # Передаем request в контекст сериализатора
    hero_data = ReachUsHeroSectionSerializer(hero, context={'request': request}).data if hero else {}
    second_data = ReachUsSecondSectionSerializer(second_section, context={'request': request}).data if second_section else {}

    return Response({
        "hero": hero_data,
        "secondSection": second_data
    })
