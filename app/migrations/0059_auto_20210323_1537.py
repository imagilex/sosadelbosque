# Generated by Django 3.0.7 on 2021-03-23 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initsys', '0003_auto_20190723_1358'),
        ('app', '0058_auto_20210315_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tmpreportecontrolrecepcion',
            options={'ordering': ['-fecha_de_ultimo_contacto']},
        ),
        migrations.AddField(
            model_name='tmpreportecontrolinscritosmod40',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportecontrolinscritosmod40detalle',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportecontrolpatronsustituto',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportecontrolpatronsustitutodetalle',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportecontrolproximopensionmod40',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportpensionesenproceso',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreportpensionesenprocesodetalle',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tmpreporttramitesycorrecciones',
            name='autor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='initsys.Usr'),
            preserve_default=False,
        ),
    ]
