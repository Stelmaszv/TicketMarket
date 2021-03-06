# Generated by Django 3.0.2 on 2020-01-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_auto_20200122_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='transportticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.BigIntegerField(max_length=100)),
                ('stan', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='route',
            name='tickets',
        ),
        migrations.AddField(
            model_name='route',
            name='tickets',
            field=models.ManyToManyField(blank=True, to='app.transportticket'),
        ),
    ]
