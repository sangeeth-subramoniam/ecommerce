# Generated by Django 3.2.7 on 2021-09-27 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0023_remove_products_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
