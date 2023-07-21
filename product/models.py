from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(verbose_name="I's Active")

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Date Time Updated')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='category', verbose_name='Category', null=True, blank=True)
    title = models.CharField(max_length=30, verbose_name='Title')
    short_description = models.TextField(verbose_name='Short Description', blank=True, null=True)
    image = models.ImageField(verbose_name='Image', upload_to='Image/Products', null=True)
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(verbose_name='Price', null=True)
    active = models.BooleanField(verbose_name="I's Active")

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Date Time Updated')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, max_length=50, related_name="comments",
                             verbose_name='Author')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", verbose_name='Product')
    message = models.TextField(verbose_name='Message')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='reply', null=True, blank=True,
                               verbose_name='Reply comment')
    active = models.BooleanField(default=True, verbose_name='Its Active')

    datetime_created_comment = models.DateTimeField(auto_now_add=True, verbose_name='Time created', editable=True)

    def __str__(self):
        return self.message
