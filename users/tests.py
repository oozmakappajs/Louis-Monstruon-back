import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Users
from .serializers import UsersSerializer

# initialize the APIClient app
client = Client()


class GetAllusersTest(TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        Users.objects.create(
            email='example@example.com', password= 'muyseguro', first_name='Juan', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')
        Users.objects.create(
            email='example2@example.com', password= 'muyseguro', first_name='Pedro', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')

    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('get_post_users'))
        # get data from db
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleUserTest(TestCase):
    """ Test module for GET single user API """

    def setUp(self):
        self.juan = Users.objects.create(
            email='example@example.com', password= 'muyseguro', first_name='Juan', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')
        self.pedro = Users.objects.create(
            email='example2@example.com', password= 'muyseguro', first_name='Pedro', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')

    def test_get_valid_single_Users(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': self.juan.pk}))
        users = Users.objects.get(pk=self.juan.pk)
        serializer = UsersSerializer(users)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_Users(self):
        response = client.get(
            reverse('get_delete_update_user', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewUserTest(TestCase):
    """ Test module for inserting a new user """

    def setUp(self):
        self.valid_payload = {
            'email': 'example@example.com',
            'password': 'muydificil',
            'first_name': 'Pedro',
            'last_name': 'Perez',
            'email_verified': False,
            'registrationDate': True,
            'phone': '123-456789'
        }
        self.invalid_payload = {
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': 'Perez',
            'email_verified': False,
            'registrationDate': True,
            'phone': '123-456789'
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleUserTest(TestCase):
    """ Test module for updating an existing user record """

    def setUp(self):
        self.juan = Users.objects.create(
            email='example@example.com', password= 'muyseguro', first_name='Juan', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')
        self.pedro = Users.objects.create(
            email='example2@example.com', password= 'muyseguro', first_name='Pedro', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')
        self.valid_payload = {
            'email': 'example@example.com',
            'password': 'muydificil',
            'first_name': 'Pedro',
            'last_name': 'Perez',
            'email_verified': False,
            'registrationDate': True,
            'phone': '123-456789'
        }
        self.invalid_payload = {
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': 'Perez',
            'email_verified': False,
            'registrationDate': True,
            'phone': '123-456789'
        }

    def test_valid_update_puppy(self):
        response = client.put(
            reverse('get_delete_update_user', kwargs={'pk': self.juan.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_user(self):
        response = client.put(
            reverse('get_delete_update_user', kwargs={'pk': self.juan.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleUserTest(TestCase):
    """ Test module for deleting an existing user record """

    def setUp(self):
        self.juan = Users.objects.create(
            email='example@example.com', password= 'muyseguro', first_name='Juan', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')
        self.pedro = Users.objects.create(
            email='example2@example.com', password= 'muyseguro', first_name='Pedro', last_name='Perez', email_verified = False, registrationDate = True, phone='123456789')

    def test_valid_delete_user(self):
        response = client.delete(
            reverse('get_delete_update_user', kwargs={'pk': self.juan.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_user', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)