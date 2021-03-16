# Generated by Django 3.0.7 on 2021-03-15 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initsys', '0003_auto_20190723_1358'),
        ('app', '0057_tmpreportecontrolinscritosmod40_tmpreportecontrolinscritosmod40detalle_tmpreportecontrolpatronsustit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tmpreportecontrolrecepcion',
            old_name='notas',
            new_name='nota',
        ),
        migrations.AddField(
            model_name='tmpreportecontrolrecepcion',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
    ]
