# Generated by Django 2.0 on 2021-11-22 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('ID_Actividad', models.AutoField(primary_key=True, serialize=False)),
                ('Descripción', models.TextField()),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['Descripción'],
            },
        ),
        migrations.CreateModel(
            name='Aparato',
            fields=[
                ('Codigo_Aparato', models.AutoField(primary_key=True, serialize=False)),
                ('Descripción', models.TextField()),
                ('Estado', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Aparato',
                'verbose_name_plural': 'Aparatos',
                'ordering': ['Estado'],
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('Codigo_Clase', models.AutoField(primary_key=True, serialize=False)),
                ('Horario', models.CharField(max_length=200)),
                ('Día', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
                'ordering': ['Día'],
            },
        ),
        migrations.CreateModel(
            name='Clases_Socios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripción', models.TextField()),
                ('Codigo_Clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Clase')),
            ],
            options={
                'verbose_name': 'Socio-Actividad',
                'verbose_name_plural': 'Socios Actividades',
                'ordering': ['Descripción'],
            },
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('DNI_E', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200)),
                ('Apellido', models.CharField(max_length=200)),
                ('Titulación', models.CharField(max_length=200)),
                ('Experiencia_Profesional', models.CharField(max_length=200)),
                ('Telefono', models.CharField(max_length=200)),
                ('Codigo_Clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Clase')),
            ],
            options={
                'verbose_name': 'Entrenador',
                'verbose_name_plural': 'Entrenadores',
                'ordering': ['Apellido'],
            },
        ),
        migrations.CreateModel(
            name='Entrenador_Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripción', models.TextField()),
                ('DNI_E', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Entrenador')),
                ('ID_Actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Actividad')),
            ],
            options={
                'verbose_name': 'Entrenador-Actividad',
                'verbose_name_plural': 'Entrenadores-Actividades',
                'ordering': ['Descripción'],
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('NumerodeSala', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=200)),
                ('Ubicación', models.CharField(max_length=200)),
                ('Metros_Cuadrados', models.CharField(max_length=25)),
                ('Codigo_Aparato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Aparato')),
                ('Codio_Clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Clase')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
                'ordering': ['Metros_Cuadrados'],
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI_S', models.CharField(max_length=20)),
                ('Nombre', models.CharField(max_length=200)),
                ('Apellido', models.CharField(max_length=200)),
                ('Dirección', models.CharField(max_length=200)),
                ('Profesión', models.CharField(max_length=200)),
                ('CBU', models.CharField(max_length=25)),
                ('Telefono', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
                'ordering': ['Apellido'],
            },
        ),
        migrations.AddField(
            model_name='clases_socios',
            name='DNI_S',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Socio'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='Codigo_Clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gimnacio.Clase'),
        ),
    ]
