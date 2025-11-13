from django.contrib import admin
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSection, QualityThirdSectionDrop,
    QualityFourthSectionBlock
)

@admin.register(QualityHeroSection)
class QualityHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2")
    exclude = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2",
              "text")

@admin.register(QualitySecondSection)
class QualitySecondSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    exclude = ("title", "titleSpan", "text")

@admin.register(QualityThirdSectionDrop)
class QualityThirdSectionDropAdmin(admin.ModelAdmin):
    list_display = ("dropsTitle",)
    exclude = ("dropsTitle", "dropsText")

@admin.register(QualityThirdSection)
class QualityThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("dropsList",)

@admin.register(QualityFourthSectionBlock)
class QualityFourthSectionBlockAdmin(admin.ModelAdmin):
    list_display = ("key", "title")
    exclude = ("title", "titleSpan", "text")
