# Generated by Django 2.1.7 on 2019-06-07 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20190607_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialaboral',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia', to='app.Cliente'),
        ),
    ]
