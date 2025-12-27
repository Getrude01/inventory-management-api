# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'quantity', 'price', 
                 'category', 'owner', 'date_added', 'last_updated']
        read_only_fields = ['owner', 'date_added', 'last_updated']
