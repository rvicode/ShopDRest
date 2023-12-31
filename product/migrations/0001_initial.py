# Generated by Django 4.2.2 on 2023-07-10 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('active', models.BooleanField(verbose_name="I's Active")),
                ('datetime_created', models.DateTimeField(default=datetime.datetime(2023, 7, 10, 12, 50, 46, 380162, tzinfo=datetime.timezone.utc), verbose_name='Date Time Created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Date Time Updated')),
            ],
        ),
    ]
