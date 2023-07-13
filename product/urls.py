from django.urls import path

from . import views


urlpatterns = [
    path('list', views.product_list_view, name='product_list'),
    path('detail/<int:pk>', views.product_detail_view, name='product_detail'),
    path('category/list', views.category_list_view, name='category_list'),
    path('category/detail/<int:pk>', views.category_detail_view, name='category_detail'),
]
