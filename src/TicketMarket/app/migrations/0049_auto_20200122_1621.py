# Generated by Django 3.0.2 on 2020-01-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20200122_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='name2',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='stan2',
            new_name='stan',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price2',
        ),
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]