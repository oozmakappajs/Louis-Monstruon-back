from datetime import datetime
import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single product
    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    # delete a single product
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single product
    if request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_products(request):
    # get all products
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    # insert a new record for a product
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'sku': request.data.get('sku'),
            'price': int(request.data.get('price')),
            'cart_desc': request.data.get('cart_desc'),
            'short_desc': request.data.get('short_desc'),
            'long_desc': request.data.get('long_desc'),
            'image': request.data.get('image'),
            'update_date': bool(request.data.get('update_date')),
            'stock': int(request.data.get('stock')),
            'unlimited': bool(request.data.get('unlimited')),
        }
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    '''def get_post_categories(request):
        pass

    def get_filter(request):
        pass

    def get_post_cart(request):
        pass'''
