from django.test import TestCase
from .models import Products


class ProductTest(TestCase):

    def setUp(self):
        self.parameters = {
            'marca': 'Monstruon',
            'size': 'small',
            'color': 'pink',
        }

    def test_output(self):
        output_answer = Products(self.parameters['marca'], self.parameters['size'], self.parameters['color'])
        self.assertEqual = (output_answer, 'Monstruon', 'small', 'pink')

    def tearDown(self):
        del self.parameters
