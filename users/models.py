from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_verified = models.BooleanField(False)
    registrationDate = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=12)


class Address(models.Model):
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    description = models.CharField(max_length=200)


class AddressUsers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)


class Orders(models.Model):
    class Transport(models.IntegerChoices):
        SHIP = 1
        AIR = 2
        LAND = 3

    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    shipping = models.IntegerField(choices=Transport.choices)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    shipped = models.BooleanField(False)
    tracking_number = models.CharField(max_length=15)
