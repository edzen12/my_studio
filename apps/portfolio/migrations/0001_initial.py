# Generated by Django 3.1.7 on 2021-03-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('steak', models.CharField(max_length=100, verbose_name='Исп. стеки')),
                ('image', models.ImageField(upload_to='portfolio/', verbose_name='Фото')),
                ('link_portfolio', models.CharField(max_length=255, verbose_name='Ссылка на проект')),
            ],
        ),
    ]
