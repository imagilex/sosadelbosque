# Generated by Django 3.0.7 on 2022-07-27 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0070_auto_20220727_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuantiabasica',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cuantiabasica',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='cuantiabasica',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cuantiabasica',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='factoredad',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='factoredad',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='factoredad',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='factoredad',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='uma',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='uma',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='uma',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='uma',
            name='updated_by',
        ),
    ]
