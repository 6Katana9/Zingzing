from django.contrib import admin
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSection, QualityThirdSectionDrop,
    QualityFourthSectionBlock
)

@admin.register(QualityHeroSection)
class QualityHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2")
    fields = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2",
              "text", "leftSideImage1", "leftSideImage2", "leftSideImage3", "rightSideImage")

@admin.register(QualitySecondSection)
class QualitySecondSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    fields = ("image", "title", "titleSpan", "text")

@admin.register(QualityThirdSectionDrop)
class QualityThirdSectionDropAdmin(admin.ModelAdmin):
    list_display = ("dropsTitle",)
    fields = ("image", "dropsTitle", "dropsText")

@admin.register(QualityThirdSection)
class QualityThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("dropsList",)

@admin.register(QualityFourthSectionBlock)
class QualityFourthSectionBlockAdmin(admin.ModelAdmin):
    list_display = ("key", "title")
    fields = ("key", "image", "title", "titleSpan", "text")
