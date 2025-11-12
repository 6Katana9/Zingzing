from django.contrib import admin
from .models import ReachUsHeroSection, ReachUsSecondSection

@admin.register(ReachUsHeroSection)
class ReachUsHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle",)
    exclude = ("mainTitle", "text")

@admin.register(ReachUsSecondSection)
class ReachUsSecondSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    exclude = ("title", "text")
