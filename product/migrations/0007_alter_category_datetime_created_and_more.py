# Generated by Django 4.2.2 on 2023-07-18 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 7, 36, 40, 251062, tzinfo=datetime.timezone.utc), verbose_name='Date Time Created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 7, 36, 40, 252993, tzinfo=datetime.timezone.utc), verbose_name='Time created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 7, 36, 40, 251640, tzinfo=datetime.timezone.utc), verbose_name='Date Time Created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='Product/img', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
    ]
