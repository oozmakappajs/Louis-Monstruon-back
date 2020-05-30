from django.db import models

from users.models import Users, Orders


class Categories(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Subcategories(models.Model):
    category = models.ForeignKey(Categories, models.PROTECT)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Products(models.Model):
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
    subcategory = models.ForeignKey(Subcategories, models.PROTECT, null=True)


class Promotion(models.Model):
    product = models.ForeignKey(Products, models.PROTECT)
    begin_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    discount = models.FloatField()


class Season(models.Model):
    product = models.ForeignKey(Products, models.PROTECT)
    end_season = models.DateField()


class Favorite(models.Model):
    product = models.ForeignKey(Products, models.PROTECT)
    users = models.ForeignKey(Users, models.PROTECT)


class OrdersDetail(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
    price = models.FloatField()
    quantity = models.IntegerField()
