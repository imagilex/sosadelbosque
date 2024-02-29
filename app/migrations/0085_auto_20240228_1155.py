# Generated by Django 3.0.14 on 2024-02-28 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0084_auto_20221122_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='actualizado_por',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='datos_estadisticos',
            field=models.TextField(blank=True, verbose_name='Datos Estadísticos'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='detalle_servicio',
            field=models.TextField(blank=True, verbose_name='Detalle de Servicio'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_de_actualizacion',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='pago',
            name='cuenta',
            field=models.CharField(blank=True, choices=[('efectivo', 'Efectivo'), ('daniel azteca', 'Daniel Azteca'), ('daniel banamex', 'Daniel Banamex'), ('sosa del bosque', 'Sosa del Bosque'), ('rebeca', 'Rebeca')], default='efectivo', max_length=50),
        ),
    ]