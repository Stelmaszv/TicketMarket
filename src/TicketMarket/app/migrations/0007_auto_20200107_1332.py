# Generated by Django 3.0.2 on 2020-01-07 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_route_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.driver'),
        ),
    ]
