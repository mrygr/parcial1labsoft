# Generated by Django 4.2.4 on 2023-08-31 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminVivero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('numero_catastro', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Número de catastro de la finca')),
                ('municipio_ubicacion', models.CharField(max_length=100, verbose_name='Municipio de ubicación finca')),
                ('documento_productor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminVivero.productor')),
            ],
        ),
    ]
