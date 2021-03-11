from django.db import models



class Service(models.Model):
    COLOR = [
        ('card-bg-a', 'Синий'),
        ('card-bg-b', 'Розовый'),
        ('card-bg-c', 'Фиолетовый'),
        ('card-bg-d', 'Пурпурный'),
        ('card-bg-e', 'Небесный'),
        ('card-bg-f', 'Зеленый'),
    ]
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    color = models.CharField(verbose_name="Цвета", choices=COLOR, max_length=15)
    image = models.ImageField(verbose_name="Фото", upload_to='services/')
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Услуги"


class Help_bus(models.Model):
    COLOR = [
        ('cd2', 'Желтый'),
        ('cd3', 'Ярко-Голубой'),
        ('cd4', 'Оранжевый'),
        ('cd5', 'Розовый'),
        ('cd6', 'Ярко-Розовый'),
        ('cd7', 'Зеленый'),
        ('cd8', 'Ярко-Голубой'),
        ('cd9', 'Светлый'),
    ]
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='help/')
    color = models.CharField(choices=COLOR, max_length=20)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Бизнес сферы"
