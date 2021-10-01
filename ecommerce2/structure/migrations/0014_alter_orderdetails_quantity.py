# Generated by Django 3.2.7 on 2021-09-17 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0013_remove_orderdetails_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
