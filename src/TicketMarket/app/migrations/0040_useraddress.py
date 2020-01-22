# Generated by Django 3.0.2 on 2020-01-22 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0039_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='useraddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulding', models.BigIntegerField(default=0)),
                ('apartment', models.BigIntegerField(default=0)),
                ('postcode', models.CharField(max_length=250)),
                ('street', models.CharField(max_length=250)),
                ('phon', models.CharField(max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]