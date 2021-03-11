from django.db import models


class Team(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to="team/")
    name = models.CharField(verbose_name="Имя", max_length=50)
    steak = models.CharField(verbose_name="Исп. стеки", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Команда"


class Statistic(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to="statictic/")
    title = models.CharField(verbose_name="Имя", max_length=50)
    numb = models.CharField(verbose_name="Цифры", max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Команда"