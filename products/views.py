from django.shortcuts import render
from rest_framework import viewsets
from .models import Dress
from .serializers import DressSerializar

class DressViewSet(viewsets.ModelViewSet):
    serializer_class = DressSerializar
    queryset = Dress.objects.all()


# Create your views here.
