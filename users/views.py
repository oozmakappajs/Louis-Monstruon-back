from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UsersSerializar

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializar
    queryset = Users.objects.all()


# Create your views here.