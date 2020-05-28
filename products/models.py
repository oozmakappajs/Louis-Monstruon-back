from django.db import models


class Products(models.Model):
    productId = models.IntegerField(max_length=5, primary_key=True)
    productName = models.CharField(max_length=50)
    productSKU = models.CharField(max_length=50)
    productPrice = models.FloatField()
    productCartDesc = models.CharField(max_length=20)
    productShortDesc = models.CharField(max_length=50)
    productLongDesc = models.CharField(max_length=200)
    productImage = models.URLField(max_length=200)
    productUpdateDate = models.DateField(auto_now=True)
    productStock = models.IntegerField(max_length=5)
    productUnlimited = models.BooleanField(False)

    def __str__(self):
        return self.productId
