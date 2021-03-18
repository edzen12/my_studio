from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Price(models.Model):
    title = models.CharField(verbose_name="Название тарифа", max_length=50)
    sub_title = models.CharField(verbose_name="Под название", max_length=50)
    price = models.FloatField(verbose_name="Цена")
    desc_list = RichTextUploadingField(verbose_name="Описание услуги")
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("price_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Цена услуг"