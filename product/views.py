from rest_framework.views import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductListSerializer


@api_view(['GET'])
def product_list_view(request):
    if request.method == 'GET':
        product = Product.objects.filter(active=True)
        ser = ProductListSerializer(product, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Please create the GET method'})
