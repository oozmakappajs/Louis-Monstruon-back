from rest_framework import serializers
from .models import Dress

class DressSerializar(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = '__all__'