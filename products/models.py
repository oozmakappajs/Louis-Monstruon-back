from django.db import models


class Products(models.Model):
    class Category(models.TextChoices):
        HOMBRE = 'hombre'
        MUJER = 'mujer'
        NIÑO = 'niño'
        ACCESORIOS = 'accesorios'

    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.FloatField()
    cart_desc = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=50)
    long_desc = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    update_date = models.DateField(auto_now=True)
    stock = models.IntegerField(blank=True, null=True)
    unlimited = models.BooleanField(False)
    category = models.TextField(choices=Category.choices, default= 'hombre')


