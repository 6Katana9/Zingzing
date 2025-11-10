from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ReachUsHeroSection, ReachUsSecondSection
from .serializers import ReachUsHeroSectionSerializer, ReachUsSecondSectionSerializer

@api_view(['GET'])
def reachus_page(request):
    hero = ReachUsHeroSection.objects.first()
    second_section = ReachUsSecondSection.objects.first()

    return Response({
        "hero": ReachUsHeroSectionSerializer(hero).data if hero else {},
        "secondSection": ReachUsSecondSectionSerializer(second_section).data if second_section else {}
    })
