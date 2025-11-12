from modeltranslation.translator import register, TranslationOptions
from .models import (
    HeroSection, SecondSectionSmallCard, ThirdSectionBigCard, FourthSectionGrowTogether
)

# ✅ HeroSection
@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'title1',
        'mainTitleSpan1',
        'title2',
        'mainTitleSpan2',
    )

# ✅ SecondSectionSmallCard
@register(SecondSectionSmallCard)
class SecondSectionSmallCardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
    )

# ✅ ThirdSectionBigCard
@register(ThirdSectionBigCard)
class ThirdSectionBigCardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )

# ✅ FourthSectionGrowTogether
@register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )
