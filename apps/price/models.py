from django.db import models


class Price(models.Model):
    title = models.CharField(verbose_name="Название тарифа", max_length=50)
    sub_title = models.CharField(verbose_name="Под название", max_length=50)
    price = models.FloatField(verbose_name="Цена")
    desc_list = models.TextField(verbose_name="Описание услуги")
    active_color = models.CharField(verbose_name="Активный тариф", max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Цена услуг"