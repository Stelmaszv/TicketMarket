# Generated by Django 3.0.2 on 2020-01-22 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20200122_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
    ]