import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Products
from ..serializers import ProductsSerializer


# initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Products.objects.create(
            productName='Dress', productSKU="Black", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productName='Dress', productSKU="Pink", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productName='Socks', productSKU="Red", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productName='T shirt', productSKU="Green", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('get_post_products'))
        # get data from db
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
