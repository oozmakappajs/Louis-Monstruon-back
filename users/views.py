from django.shortcuts import render
from rest_framework import viewsets

from .models import Users
from .serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
