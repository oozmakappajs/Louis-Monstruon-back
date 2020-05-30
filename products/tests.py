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
            name='Dress', sku="Black", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        Products.objects.create(
            name='Dress', sku="Pink", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        Products.objects.create(
            name='Socks', sku="Red", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        Products.objects.create(
            name='T shirt', sku="Green", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)

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
            name='Dress', sku="Black", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        self.dress2 = Products.objects.create(
            name='Dress', sku="Pink", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        self.socks = Products.objects.create(
            name='Socks', sku="Red", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        self.tshirt = Products.objects.create(
            name='T shirt', sku="Green", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)

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
            'name': 'Dress',
            'sku': 'Black',
            'price': 25,
            'cart_desc': 'This is the cart description',
            'short_desc': 'This is the short description',
            'long_desc': 'This is the long description',
            'image': 'https://www.gstatic.com/webp/gallery3/1.png',
            'update_date': True,
            'stock': 3,
            'unlimited': False,
        }

        self.invalid_payload = {
            'name': 25,
            'sku': '',
            'price': '',
            'cart_desc': 'This is the cart description',
            'short_desc': 'This is the short description',
            'long_desc': 'This is the long description',
            'image': '',
            'update_date': '',
            'stock': 3 ,
            'unlimited': False,
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

    class UpdateSingleProductTest(TestCase):
        """ Test module for updating an existing product record """

    def setUp(self):
        self.dress = Products.objects.create(
            name='Dress', sku="Black", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5.0, unlimited=False)
        self.dress2 = Products.objects.create(
            name='Dress', sku="Pink", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5.0, unlimited=False)
        self.valid_payload = {
            'name': 'Dress',
            'sku': 'Blue',
            'price': 30,
            'cart_desc': 'This is the cart description',
            'short_desc': 'This is the short description',
            'long_desc': 'This is the long description',
            'image': 'https://www.gstatic.com/webp/gallery3/1.png',
            'update_date': True,
            'stock': 3,
            'unlimited': False,
        }

        self.invalid_payload = {
            'name': '',
            'sku': '',
            'price': 25,
            'cart_desc': 'This is the cart description',
            'short_desc': 'This is the short description',
            'long_desc': 'This is the long description',
            'image': 'https://www.gstatic.com/webp/gallery3/1.png',
            'update_date': True,
            'stock': 3,
            'unlimited': False,
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
            name='Dress', sku="Black", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)
        self.dress2 = Products.objects.create(
            name='Dress', sku="Pink", price=25, cart_desc='This is the description', short_desc="This is thr short description", long_desc="This is the long description", image="https://www.gstatic.com/webp/gallery3/1.png", update_date= True, stock=5, unlimited=False)

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.dress.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)