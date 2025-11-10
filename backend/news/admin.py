from django.contrib import admin
from .models import NewsHeroSection, NewsSecondSection, NewsSecondBlock

@admin.register(NewsHeroSection)
class NewsHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle", "titleSpan1", "titleSpan2")
    fields = ("mainTitle", "titleSpan1", "titleSpan2", "text",
              "leftSideImage1", "leftSideImage2", "leftSideImage3", "rightSideImage")

@admin.register(NewsSecondBlock)
class NewsSecondBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    fields = ("title", "titleSpan", "text", "image")

@admin.register(NewsSecondSection)
class NewsSecondSectionAdmin(admin.ModelAdmin):
    fields = ("firstBlock", "secondBlock", "thirdBlock")
