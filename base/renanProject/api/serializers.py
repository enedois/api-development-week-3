from rest_framework import serializers
from renanBase.models import Product

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'