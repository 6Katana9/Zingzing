from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeChoices(models.IntegerChoices):
    HEADER = 0, _('Заголовок')          # Главный заголовок страницы
    REVIEWS = 1, _('Отзывы')            # Блок отзывов
    HERO_SECTION = 2, _('Баннер / главный блок')  # Верхний баннер или "герой"
    COUNTRIES = 3, _('Страны')          # Секция со странами
    PRODUCTS = 4, _('Продукты')         # Блок с продуктами
    MATRYOSHKA = 5, _('Матрешки')  
    OTHER_BLOCK = 6, _('Доп блоки')