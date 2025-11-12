from modeltranslation.translator import register, TranslationOptions
from .models import HeroSection, SecondSection, CountryItem, DropsItem, ThirdBlock

# ✅ HeroSection
@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'title1',
        'mainTitleSpan1',
        'title2',
        'mainTitleSpan2',
        'text',
    )

# ✅ CountryItem
@register(CountryItem)
class CountryItemTranslationOptions(TranslationOptions):
    fields = (
        'innerTitle',
        'text',
    )

# ✅ DropsItem
@register(DropsItem)
class DropsItemTranslationOptions(TranslationOptions):
    fields = (
        'dropsTitle',
        'dropsText',
    )

# ✅ SecondSection
@register(SecondSection)
class SecondSectionTranslationOptions(TranslationOptions):
    fields = (
        'mainTitle',
        'mainTitleSpan',
    )

# ✅ ThirdBlock
@register(ThirdBlock)
class ThirdBlockTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )
