# Generated by Django 3.2.7 on 2021-09-24 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_user_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]