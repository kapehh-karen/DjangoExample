from django.db import models


# Create your models here.

class Film(models.Model):
    title = models.TextField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", max_length=(1024 * 4))
    picture = models.ImageField(verbose_name="Постер", upload_to="film_pics/", blank=True)

    def __str__(self):
        return self.title
