# Generated by Django 3.0.14 on 2022-10-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0074_incrementomodalidad40'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incrementomodalidad40',
            name='sdi',
        ),
        migrations.AddField(
            model_name='incrementomodalidad40',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Monto Mensual'),
        ),
    ]
