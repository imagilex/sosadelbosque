# Generated by Django 3.0.7 on 2021-04-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_tmpreportecontrolinscritosmod40_fecha_de_alta'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpEstatusEnvio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['medio'],
            },
        ),
        migrations.CreateModel(
            name='TmpMedioInscMod40',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['medio'],
            },
        ),
        migrations.CreateModel(
            name='TmpMedioPatronSustituto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['medio'],
            },
        ),
        migrations.CreateModel(
            name='TmpProxEvt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medio', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['medio'],
            },
        ),
        migrations.RemoveField(
            model_name='tmpreportecontrolinscritosmod40detalle',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='tmpreportecontrolinscritosmod40detalle',
            name='linea_de_captura',
        ),
        migrations.AlterField(
            model_name='tmpreportecontrolinscritosmod40',
            name='medio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='app.TmpMedioInscMod40'),
        ),
        migrations.AlterField(
            model_name='tmpreportecontrolinscritosmod40detalle',
            name='estatus_de_envio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='app.TmpEstatusEnvio'),
        ),
        migrations.AlterField(
            model_name='tmpreportecontrolpatronsustituto',
            name='medio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='app.TmpMedioPatronSustituto'),
        ),
        migrations.AlterField(
            model_name='tmpreportecontrolproximopensionmod40',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='app.TmpProxEvt'),
        ),
    ]
