from django.db import models


class Setting(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название сайта")
    logo = models.ImageField(verbose_name="Логотип сайта", upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name="Описание сайта", blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=100, verbose_name="Адрес")
    phone_1 = models.CharField(blank=True, null=True, max_length=14, verbose_name="Номер телефона 1")
    phone_2 = models.CharField(blank=True, null=True, max_length=14, verbose_name="Номер телефона 2")
    email = models.CharField(blank=True, null=True, max_length=255, verbose_name="E-mail")

    whatsapp = models.CharField(blank=True, null=True, max_length=13, verbose_name="WhatsApp номер")
    instagram = models.CharField(blank=True,null=True, max_length=255, verbose_name="Instagram ссылка")
    telegram = models.CharField(blank=True, null=True, max_length=255, verbose_name="Telegram для связи")

    aboutus_page = models.TextField(verbose_name="О нас", blank=True, null=True)

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Основные настройки"
