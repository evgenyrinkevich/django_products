from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.db.models import Manager


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    measure = models.CharField(max_length=128, verbose_name='единица измерения')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена')
    receipt_date = models.DateField(auto_now_add=True, verbose_name='дата поступления')
    supplier = models.CharField(max_length=128, verbose_name='поставщик')
    category = models.ManyToManyField('Category')
    sites = models.ManyToManyField(Site)
    objects = Manager()
    on_site = CurrentSiteManager('sites')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    description = models.TextField(blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
