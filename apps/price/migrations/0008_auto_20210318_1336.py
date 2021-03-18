# Generated by Django 3.1.7 on 2021-03-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_remove_price_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Цена услуг'},
        ),
        migrations.AddField(
            model_name='price',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
