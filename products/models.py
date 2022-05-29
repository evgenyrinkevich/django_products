from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    measure = models.CharField(max_length=128, verbose_name='единица измерения')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена')
    receipt_date = models.DateField(auto_now_add=True, verbose_name='дата поступления')
    supplier = models.CharField(max_length=128, verbose_name='поставщик')
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
