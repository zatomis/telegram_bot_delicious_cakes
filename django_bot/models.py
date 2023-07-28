from django.db import models


class TelegramUser(models.Model):
    chat_id = models.CharField(
        max_length=20
    )

    def __str__(self) -> str:
        return self.chat_id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save()


class Catalog(models.Model):
    image = models.ImageField(upload_to="images/")
    price = models.IntegerField(default=0)
    short_title = models.CharField(max_length=30) 
    description = models.TextField()

    def __str__(self):
        return f'{self.short_title} {self.price}'

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Список тортов"
