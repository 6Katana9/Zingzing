from django.contrib import admin
from .models import Product, Page, Element, Files

# ------------------------
# Inline для элементов на странице
# ------------------------
class ElementInline(admin.TabularInline):
    model = Element
    extra = 1
    show_change_link = True
    filter_horizontal = ('products', 'files')
    fields = ('type', 'title', 'description', 'photo', 'is_active', 'products', 'files')

# ------------------------
# Page admin
# ------------------------
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ElementInline]

# ------------------------
# Element admin
# ------------------------
@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'type', 'is_active')
    list_filter = ('page', 'type', 'is_active')
    search_fields = ('title', 'description', 'page__name')
    filter_horizontal = ('products', 'files')

# ------------------------
# Product admin
# ------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

# ------------------------
# Files admin
# ------------------------
@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('file',)
