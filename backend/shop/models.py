from django.db import models

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