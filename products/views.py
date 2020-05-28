from datetime import datetime
import json

from django.http import HttpResponse
from rest_framework import viewsets

from .models import Products
from .serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


def allProducts(request):
    type_response = ''
    if request.method == 'GET':
        type_response = 'Todo bien'

    data = {
        'status': 'OK',
        'type_response': type_response,
        'message': 'Todo salio bien'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def oneProduct(request, id):
    if request.method == 'GET':
        type_response = 'solo un producto por aqui '
    data = {
        'status': 'OMG',
        'type_response': type_response + str(id),
        'message': 'Un mensaje mas'
    }

    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
