# Generated by Django 3.0.4 on 2020-05-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20200117_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fecha',
            field=models.DateField(blank=True, default=None, null=True),
            preserve_default=False,
        ),
    ]
