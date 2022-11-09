# Generated by Django 3.0.14 on 2022-11-01 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_auto_20221025_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idpago', models.AutoField(primary_key=True, serialize=False)),
                ('concepto', models.CharField(max_length=250)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha_de_pago', models.DateTimeField(blank=True)),
                ('estatus', models.CharField(choices=[('pendiente', 'Pendiente de Pago'), ('pagado', 'Pagado')], max_length=20)),
                ('codigo', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='app.Cliente')),
            ],
        ),
    ]