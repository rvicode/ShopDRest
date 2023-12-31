# Generated by Django 4.2.2 on 2023-07-12 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_active_category_datetime_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='category', to='product.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 13, 7, 4, 570634, tzinfo=datetime.timezone.utc), verbose_name='Date Time Created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 13, 7, 4, 571194, tzinfo=datetime.timezone.utc), verbose_name='Date Time Created'),
        ),
    ]
