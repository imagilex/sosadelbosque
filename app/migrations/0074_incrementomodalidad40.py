# Generated by Django 3.0.14 on 2022-10-18 16:06

import app.models_inc_mod40
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_auto_20221018_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncrementoModalidad40',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inicio', models.PositiveSmallIntegerField(default=app.models_inc_mod40.inicio_yr, verbose_name='Año de Inicio')),
                ('fin', models.PositiveSmallIntegerField(default=app.models_inc_mod40.fin_yr, verbose_name='Año de Termino')),
                ('tipo', models.CharField(choices=[('inicio', 'Pago al inicio'), ('fin', 'Pago al término')], default=models.PositiveSmallIntegerField(default=app.models_inc_mod40.inicio_yr, verbose_name='Año de Inicio'), max_length=10)),
                ('sdi', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incrementos_m40', to='app.Cliente')),
            ],
        ),
    ]