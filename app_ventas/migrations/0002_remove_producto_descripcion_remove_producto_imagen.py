# Generated by Django 4.2.4 on 2023-08-16 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
