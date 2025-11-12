from modeltranslation.translator import register, TranslationOptions
from .models import NewsHeroSection, NewsSecondBlock, NewsSecondSection

# ✅ NewsHeroSection
@register(NewsHeroSection)
class NewsHeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'mainTitle',
        'titleSpan1',
        'titleSpan2',
        'text',
    )

# ✅ NewsSecondBlock
@register(NewsSecondBlock)
class NewsSecondBlockTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )

# ✅ NewsSecondSection
# тут поля для перевода нет, так как все текстовые данные внутри блоков
# связь с блоками останется без изменений
