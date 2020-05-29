from django.test import TestCase
from .models import Users


'''class UserTest(TestCase):

    def setUp(self):
        self.parameters = {
            'name': 'Jose',
            'surname': 'jose123',
            'password': 'seguro',
            'address': 'Montevideo 5'
        }

    def test_output(self):
        output_answer = Users(self.parameters['name'], self.parameters['surname'], self.parameters['password'], self.parameters['address'])
        self.assertEqual = (output_answer, 'Jose', 'jose123', 'seguro', 'Montevideo 5') 
        
    def tearDown(self):
            del(self.parameters)'''