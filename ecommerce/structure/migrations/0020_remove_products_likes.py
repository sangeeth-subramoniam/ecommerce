# Generated by Django 3.2.7 on 2021-09-27 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0019_alter_reviews_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='likes',
        ),
    ]
