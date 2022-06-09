# Generated by Django 4.0.5 on 2022-06-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasajeros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='cedula',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='correo',
            field=models.EmailField(max_length=120, unique=True),
        ),
    ]
