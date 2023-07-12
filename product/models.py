from django.db import models

from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    active = models.BooleanField(verbose_name="I's Active")

    datetime_created = models.DateTimeField(default=timezone.now(), verbose_name='Date Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Date Time Updated')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    active = models.BooleanField(verbose_name="I's Active")

    datetime_created = models.DateTimeField(default=timezone.now(), verbose_name='Date Time Created')
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name='Date Time Updated')

    def __str__(self):
        return self.title
