from django.contrib import admin
from .models import NewsHeroSection, NewsSecondSection, NewsSecondBlock

@admin.register(NewsHeroSection)
class NewsHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle", "titleSpan1", "titleSpan2")
    exclude = ("mainTitle", "titleSpan1", "titleSpan2", "text")

@admin.register(NewsSecondBlock)
class NewsSecondBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    exclude = ("title", "titleSpan", "text")

@admin.register(NewsSecondSection)
class NewsSecondSectionAdmin(admin.ModelAdmin):
    fields = ("firstBlock", "secondBlock", "thirdBlock")
