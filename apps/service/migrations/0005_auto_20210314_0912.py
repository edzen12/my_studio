# Generated by Django 3.1.7 on 2021-03-14 09:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_my_steak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
