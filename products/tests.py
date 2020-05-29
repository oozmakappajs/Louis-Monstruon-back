import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Products
from .serializers import ProductsSerializer


# initialize the APIClient app
client = Client()

class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Products.objects.create(
            productId=1,productName='Dress', productSKU="Black", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productId=2,productName='Dress', productSKU="Pink", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productId=3,productName='Socks', productSKU="Red", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        Products.objects.create(
            productId=4,productName='T shirt', productSKU="Green", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('get_post_products'))
        # get data from db
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):
    """ Test module for GET single product API """

    def setUp(self):
        self.dress = Products.objects.create(
            productId=1,productName='Dress', productSKU="Black", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.dress2 = Products.objects.create(
            productId=2,productName='Dress', productSKU="Pink", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.socks = Products.objects.create(
            productId=3,productName='Socks', productSKU="Red", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.tshirt = Products.objects.create(
            productId=4,productName='T shirt', productSKU="Green", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': self.dress.pk}))
        product = Products.objects.get(pk=self.dress.pk)
        serializer = ProductsSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'productId': '1',
            'productName': 'Dress',
            'productSKU': 'Black',
            'productPrice': 25,
            'productCartDesc': 'This is the cart description',
            'productShortDesc': 'This is the short description',
            'productLongDesc': 'This is the long description',
            'productImage': 'www.example.com',
            'productUpdateDate': True,
            'productStock': 3,
            'productUnlimited': False,
        }

        self.invalid_payload = {
            'productId': '',
            'productName': '',
            'productSKU': '',
            'productPrice': 25,
            'productCartDesc': 'This is the cart description',
            'productShortDesc': 'This is the short description',
            'productLongDesc': 'This is the long description',
            'productImage': 'www.example.com',
            'productUpdateDate': True,
            'productStock': 3,
            'productUnlimited': False,
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    class UpdateSinglePuppyTest(TestCase):
        """ Test module for updating an existing product record """

    def setUp(self):
        self.dress = Products.objects.create(
            productId=1,productName='Dress', productSKU="Black", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.dress2 = Products.objects.create(
            productId=2,productName='Dress', productSKU="Pink", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.valid_payload = {
            'productId': '2',
            'productName': 'Dress',
            'productSKU': 'Blue',
            'productPrice': 30,
            'productCartDesc': 'This is the cart description',
            'productShortDesc': 'This is the short description',
            'productLongDesc': 'This is the long description',
            'productImage': 'www.example.com',
            'productUpdateDate': True,
            'productStock': 3,
            'productUnlimited': False,
        }

        self.invalid_payload = {
            'productId': '',
            'productName': '',
            'productSKU': '',
            'productPrice': 25,
            'productCartDesc': 'This is the cart description',
            'productShortDesc': 'This is the short description',
            'productLongDesc': 'This is the long description',
            'productImage': 'www.example.com',
            'productUpdateDate': True,
            'productStock': 3,
            'productUnlimited': False,
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.dress.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.dress.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePuppyTest(TestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.dress = Products.objects.create(
            productId=1,productName='Dress', productSKU="Black", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)
        self.dress2 = Products.objects.create(
            productId=2,productName='Dress', productSKU="Pink", productPrice=25, productCartDesc='This is the description', productShortDesc="This is thr short description", productLongDesc="This is the long description", productImage="www.example.com", productUpdateDate= True, productStock=5, productUnlimited=False)

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.dress.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)