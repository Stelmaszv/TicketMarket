# Generated by Django 3.0.2 on 2020-01-31 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20200131_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.company'),
        ),
    ]
