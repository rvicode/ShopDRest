from django.urls import path

from . import views


urlpatterns = [
    path('list', views.product_list_view, name='product_list'),
]
