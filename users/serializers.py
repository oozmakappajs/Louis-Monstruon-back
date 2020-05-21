from rest_framework import serializers
from .models import Users

class UsersSerializar(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'