from modeltranslation.translator import register, TranslationOptions
from .models import (
    HeroSection, FirstSection,
    SecondSectionCard, SecondSection,
    ThirdSectionCard, ThirdSection,
    FourthSectionGrowTogether
)

# ✅ HeroSection
@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'mainTitle',
        'mainTitleSpan1',
        'mainTitleSpan2',
        'firstText',
        'secondText',
    )

# ✅ FirstSection
@register(FirstSection)
class FirstSectionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )

# ✅ SecondSectionCard
@register(SecondSectionCard)
class SecondSectionCardTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'text',
    )

# ✅ SecondSection
@register(SecondSection)
class SecondSectionTranslationOptions(TranslationOptions):
    fields = ('mainTitle',)

# ✅ ThirdSectionCard
@register(ThirdSectionCard)
class ThirdSectionCardTranslationOptions(TranslationOptions):
    fields = ('text',)

# ✅ ThirdSection
# нет полей для перевода, только связь с карточками

# ✅ FourthSectionGrowTogether
@register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherTranslationOptions(TranslationOptions):
    fields = ('title', 'titleSpan', 'text')
