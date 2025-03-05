from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    review = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.title
