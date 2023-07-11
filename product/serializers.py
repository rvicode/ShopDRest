from rest_framework import serializers

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'datetime_created')
        read_only = True


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'datetime_created')
        read_only = True
