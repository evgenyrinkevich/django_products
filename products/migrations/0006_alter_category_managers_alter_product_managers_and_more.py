# Generated by Django 4.0.4 on 2022-06-03 09:06

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_sites'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('sites')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default="[PosixPath('/home/evgeny/PycharmProjects/djangoProject/media')]/default_product.png", upload_to=[pathlib.PurePosixPath('/home/evgeny/PycharmProjects/djangoProject/media')], verbose_name='изображение'),
        ),
    ]
