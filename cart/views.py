from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from product.models import Product
from .cart import Cart
from .serializers import CartProductSerializer


@api_view(['POST'])
def add_to_cart_view(request, product_id=None, quantity=None):
    if request.user.is_authenticated:
        cart = Cart(request)

        product = get_object_or_404(Product, id=product_id)
        quantity_number = int(quantity)
        inplace = request.POST.get('inplace')

        if product and quantity_number:
            if inplace:
                cart.add(product, quantity_number, replace_current_quantity=inplace)
            else:
                cart.add(product, quantity_number)

            return Response({'success': 'Add product to cart successfully'}, status=status.HTTP_200_OK)

        else:
            return Response({'Error': 'Form not Valid!'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'error authenticate': 'User is not login'}, status=status.HTTP_401_UNAUTHORIZED)


class CartDetailView(APIView):
    def get(self, request):
        try:
            cart = Cart(request)
            products = list(cart)

            if cart == None or products == None:
                raise ValueError('is empty')
            
            else:
                serializer = CartProductSerializer(products, many=True, context={'cart': cart.cart})
                cart_data = {
                    'items': serializer.data,
                    'total_quantity': len(cart),
                    'total_price': cart.get_total_price(),
                }
                return Response(cart_data, status=status.HTTP_200_OK)

        except ValueError as e:
            return Response({'Cart error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET'])
def clear_all_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return Response({'Cart': 'Cart is clear'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def remove_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return Response({'Cart': f'Cart {product_id} removed'})