from rest_framework import serializers

from .models import Users, Orders, Address, AddressUsers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders 
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AddressUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressUsers
        fields = "__all__"

