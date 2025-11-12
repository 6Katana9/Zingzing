from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSection, QualityFourthSectionBlock
)
from .serializers import (
    QualityHeroSectionSerializer, QualitySecondSectionSerializer,
    QualityThirdSectionSerializer, QualityFourthSectionBlockSerializer
)

@api_view(['GET'])
def quality_page(request):
    hero = QualityHeroSection.objects.first()
    second_section = QualitySecondSection.objects.first()
    third_section = QualityThirdSection.objects.first()
    fourth_blocks = QualityFourthSectionBlock.objects.all()

    # Составляем JSON для fourthSection по ключам
    fourth_section = {
        block.key: QualityFourthSectionBlockSerializer(block, context={"request": request}).data
        for block in fourth_blocks
    }

    return Response({
        "hero": QualityHeroSectionSerializer(hero, context={"request": request}).data if hero else {},
        "secondSection": QualitySecondSectionSerializer(second_section, context={"request": request}).data if second_section else {},
        "thirdSection": QualityThirdSectionSerializer(third_section, context={"request": request}).data if third_section else {},
        "fourthSection": fourth_section
    })
