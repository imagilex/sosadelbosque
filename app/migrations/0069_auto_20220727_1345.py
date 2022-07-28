# Generated by Django 3.0.7 on 2022-07-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0068_auto_20210504_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialaboral',
            name='semanas_favor_cd',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número de Semanas a Favor CD'),
        ),
        migrations.AddField(
            model_name='historialaboral',
            name='semanas_reincorporadas',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número de Semanas Reincorporadas'),
        ),
    ]
