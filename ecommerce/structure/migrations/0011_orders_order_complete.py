# Generated by Django 3.2.7 on 2021-09-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0010_alter_orderdetails_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_complete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
