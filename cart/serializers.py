# serializers.py
from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price')

class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj['product']['price'] * obj['quantity']

class CartProductSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    total_price = serializers.SerializerMethodField()
    product_obj = ProductSerializer(source='product', read_only=True)

    class Meta:
        fields = ('product', 'quantity', 'total_price', 'product_obj')

    def get_total_price(self, obj):
        cart = self.context.get('cart', {})
        product_id = str(obj['product']['id'])
        if product_id in cart:
            return obj['product']['price'] * cart[product_id]['quantity']
        return 0
