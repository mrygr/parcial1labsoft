# Generated by Django 4.2.4 on 2023-08-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('documento_productor', models.IntegerField(primary_key=True, serialize=False, verbose_name='numero identificacion productor')),
                ('nombres_productor', models.CharField(max_length=100, verbose_name='Nombres productor')),
                ('apellidos_productor', models.CharField(max_length=100, verbose_name='Apellidos productor')),
                ('telefono_productor', models.CharField(max_length=50, verbose_name='Telefono productor')),
                ('correo_productor', models.EmailField(max_length=254, verbose_name='Email productor')),
            ],
        ),
    ]
