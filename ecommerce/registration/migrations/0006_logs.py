# Generated by Django 3.2.7 on 2021-10-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_user_profile_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('start_time', models.DateTimeField(auto_created=True, blank=True)),
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('logger', models.CharField(blank=True, max_length=100, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
