# Generated by Django 2.1.7 on 2019-12-10 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_tasks', '0001_initial'),
        ('initsys', '0003_auto_20190723_1358'),
        ('app', '0046_auto_20190926_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssocActTarea',
            fields=[
                ('idassocActTarea', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='app.Actividad')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='simple_tasks.Tarea')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['actividad', 'tarea', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssocCteTarea',
            fields=[
                ('idassocCteTarea', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('cte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='app.Cliente')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='simple_tasks.Tarea')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['cte', 'tarea', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='AssocHistLabTarea',
            fields=[
                ('idassocHistLabTarea', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
                ('historial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='app.HistoriaLaboral')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiales', to='simple_tasks.Tarea')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='initsys.Usr')),
            ],
            options={
                'ordering': ['historial', 'tarea', 'created_at'],
            },
        ),
    ]