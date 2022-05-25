from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')
    measure = models.CharField(max_length=128, verbose_name='единица измерения')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='цена')
    receipt_date = models.DateField(auto_now_add=True, verbose_name='дата поступления')
    supplier = models.CharField(max_length=128, verbose_name='поставщик')
