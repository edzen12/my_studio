from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Price(models.Model):
    title = models.CharField(verbose_name="Название тарифа", max_length=50)
    image = models.FileField(verbose_name="фото", upload_to='price/', blank=True, null=True)
    sub_title = models.CharField(verbose_name="Под название", max_length=50)
    price = models.FloatField(verbose_name="Цена")
    desc_list = RichTextUploadingField(verbose_name="Описание услуги")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Цена услуг"