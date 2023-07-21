from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from product.models import Product
from .cart import Cart


@api_view(['POST'])
def add_to_cart_view(request, product_id=None):
    if request.user.is_authenticated:
        cart = Cart(request)
        print(cart)

        product = get_object_or_404(Product, id=product_id)
        quantity_number = request.POST.get('quantity')
        inplace = request.POST.get('inplace')
        print(product)
        print(quantity_number)
        print(inplace)

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
