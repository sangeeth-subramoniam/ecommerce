# Generated by Django 3.2.7 on 2021-09-27 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0020_remove_products_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='like',
        ),
    ]
