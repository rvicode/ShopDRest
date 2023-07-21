from django.urls import path


from . import views

urlpatterns = [
   path('add/<int:product_id>', views.add_to_cart_view, name='cart_add'),
]