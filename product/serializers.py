from rest_framework import serializers

from .models import Product, Category, Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'message', 'parent', 'active', 'datetime_created_comment')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'datetime_created')
        read_only = True


class ProductDetailSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(read_only=True, many=True)
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title')

    class Meta:
        model = Product
        fields = ('category', 'id', 'title', 'description', 'active','price', 'datetime_created', 'comments')
        read_only = True


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )
        read_only = True


class CategoryDetailSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('product', )

    def get_product(self, obj):
        ser = ProductListSerializer(instance=obj.category.all(), many=True)
        return ser.data
