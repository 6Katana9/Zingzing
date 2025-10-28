from django.db import models
from .choices import TypeChoices

class Product(models.Model):
    title = models.CharField(verbose_name='Название',max_length=200)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена',default=0)
    created_at = models.DateField(verbose_name='Дата добавления',auto_now_add=True)
    image = models.ImageField(verbose_name='Изображение',upload_to='media/', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'


class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.name


class Files(models.Model):
    file = models.FileField(upload_to='files', verbose_name='Видео/Изображение')


class Element(models.Model):
    type = models.PositiveSmallIntegerField(
        'Тип элемента', blank=True, null=True,
        choices=TypeChoices.choices)
    photo = models.FileField(upload_to='photo', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="elements")
    products = models.ManyToManyField(Product,  blank=True, null=True)
    files = models.ManyToManyField(Files, blank=True, null=True)
    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"

    def __str__(self):
        return f"{self.page.name} — {self.type}"