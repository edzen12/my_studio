# Generated by Django 3.1.7 on 2021-04-18 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_filter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Портфолио'},
        ),
    ]