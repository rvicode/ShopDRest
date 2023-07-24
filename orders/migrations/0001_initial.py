# Generated by Django 4.2.2 on 2023-07-24 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is Paid?')),
                ('zarin_authority', models.CharField(blank=True, max_length=255)),
                ('zarin_ref_id', models.CharField(blank=True, max_length=150)),
                ('zarin_data', models.TextField(blank=True)),
                ('firstname', models.CharField(max_length=100, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=100, verbose_name='Last Name')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('address', models.TextField(verbose_name='Address')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='Time Created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Time Updated')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
