from django.db import models



class Portfolio(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=50)
    steak = models.CharField(verbose_name="Исп. стеки", max_length=100)
    image = models.ImageField(verbose_name="Фото", upload_to='portfolio/')
    link_portfolio = models.CharField(verbose_name="Ссылка на проект", max_length=255)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Портфолио"