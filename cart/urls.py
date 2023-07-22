from django.urls import path


from . import views

urlpatterns = [
   path('api/cart/', views.CartDetailView.as_view(), name='cart-detail'),
   path('add/<int:product_id>/<int:quantity>', views.add_to_cart_view, name='cart_add'),
   path('clear', views.clear_all_cart_view, name='cart_clear'),
   path('remove/<int:product_id>', views.remove_to_cart_view, name='cart_remove')
]