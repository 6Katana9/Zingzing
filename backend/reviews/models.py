from django.db import models

class VideoReviews(models.Model):
    video = models.FileField(upload_to='reviews/', verbose_name='Видео')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Видео отзыв {self.id}"
    
    class Meta:
        verbose_name='Видео отзыв'
        verbose_name_plural='Видео отзывы'