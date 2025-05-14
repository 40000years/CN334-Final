from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'detail', 'price', 'stock', 'categories',
            'production_date', 'expiration_date', 'address', 'available',
            'created_at', 'updated_at'
        ]