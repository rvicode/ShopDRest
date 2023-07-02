from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name=_("Email"))
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
