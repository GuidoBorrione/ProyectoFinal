# Generated by Django 2.0 on 2021-11-22 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gimnacio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='Codio_Clase',
            new_name='Codigo_Clase',
        ),
    ]