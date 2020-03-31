# Generated by Django 3.0.3 on 2020-03-30 00:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('local_name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('local_name', models.CharField(max_length=64)),
                ('lat', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('lon', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='manage_subdivisions.Subdivision')),
            ],
        ),
    ]
