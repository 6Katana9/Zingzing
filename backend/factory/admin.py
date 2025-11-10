from django.contrib import admin
from .models import HeroSection, Section, SwiperSlide

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "titleSpan1", "title2", "titleSpan2")
    fieldsets = (
        ("Titles", {
            "fields": ("title1", "titleSpan1", "title2", "titleSpan2", "text")
        }),
        ("Images", {
            "fields": ("image1", "image2", "image3")
        }),
    )

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("key", "title")
    fieldsets = (
        (None, {
            "fields": ("key", "title", "text", "image")
        }),
    )
    # Добавим фильтр по ключу, чтобы быстро находить нужную секцию
    list_filter = ("key",)

@admin.register(SwiperSlide)
class SwiperSlideAdmin(admin.ModelAdmin):
    list_display = ("alt", "image")
    fieldsets = (
        (None, {
            "fields": ("image", "alt")
        }),
    )
