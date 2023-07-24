from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from product.models import Product


class Order(models.Model):
    username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='User')
    is_paid = models.BooleanField(verbose_name='Is Paid?', default=False)

    zarin_authority = models.CharField(max_length=255, blank=True)
    zarin_ref_id = models.CharField(max_length=150, blank=True)
    zarin_data = models.TextField(blank=True)

    firstname = models.CharField(verbose_name='First Name', max_length=100)
    lastname = models.CharField(verbose_name='Last Name', max_length=100)
    phonenumber = PhoneNumberField(verbose_name='Phone Number')
    message = models.TextField(verbose_name='Message', blank=True, null=True)
    address = models.TextField(verbose_name='Address')

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Time Updated')

    def __str__(self):
        return f'Username: {self.username}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Time Updated')

    def __str__(self):
        return f'Order {self.order.id}: {self.product} , quantity: {self.quantity}, price: {self.price}'