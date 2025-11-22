from django.db import models


class PartnershipRequest(models.Model):
    email = models.EmailField("Email компании или ваш")
    phone = models.CharField("Номер телефона", max_length=30)
    message = models.TextField("Сообщение", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} — {self.phone}"