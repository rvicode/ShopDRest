from rest_framework.views import Response
from rest_framework import status
from rest_framework.decorators import api_view


from .models import Product, Category, Comment
from .serializers import ProductListSerializer, ProductDetailSerializer, CategoryListSerializer,\
    CategoryDetailSerializer,\
    CommentListSerializer


@api_view(['GET'])
def product_list_view(request):
    if request.method == 'GET':
        product = Product.objects.filter(active=True)
        ser = ProductListSerializer(product, many=True)
        return Response(data=ser.data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Please create the GET method'})


@api_view(['GET'])
def product_detail_view(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(id=pk)
        if product.active is True:
            ser = ProductDetailSerializer(product)
            return Response(data=ser.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'That is not active product'})
    else:
        return Response({'detail': 'Please create the GET method'})


@api_view(['GET'])
def category_list_view(request):
    if request.method == 'GET':
        category = Category.objects.filter(active=True)
        ser = CategoryListSerializer(category, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Please create the GET method'})


@api_view(['GET'])
def category_detail_view(request, pk):
    category = Category.objects.get(id=pk)
    ser = CategoryDetailSerializer(category)
    return Response(ser.data, status=status.HTTP_200_OK)
