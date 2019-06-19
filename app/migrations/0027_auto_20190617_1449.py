# Generated by Django 2.1.7 on 2019-06-17 19:49

import app.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('initsys', '0002_auto_20190409_1910'),
        ('app', '0026_auto_20190612_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='UMA',
            fields=[
                ('iduma', models.AutoField(primary_key=True, serialize=False)),
                ('año', models.PositiveSmallIntegerField(default=app.models.getyear, unique=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['año'],
            },
        ),
        migrations.AddField(
            model_name='historialaboralregistro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historialaboralregistro',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
        migrations.AddField(
            model_name='historialaboralregistro',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='historialaboralregistro',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
        migrations.AddField(
            model_name='historialaboralregistrodetalle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historialaboralregistrodetalle',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
        migrations.AddField(
            model_name='historialaboralregistrodetalle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='historialaboralregistrodetalle',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr'),
        ),
    ]
