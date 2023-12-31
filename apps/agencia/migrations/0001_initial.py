# Generated by Django 4.2.7 on 2023-12-20 22:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('resumen', ckeditor.fields.RichTextField()),
                ('contenido', ckeditor.fields.RichTextField()),
                ('vistas', models.PositiveIntegerField(default=0)),
                ('destacado', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('anio', models.PositiveIntegerField()),
                ('km', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transmision', models.CharField(default='Manual', max_length=20)),
                ('estado', models.CharField(default='Disponible', max_length=20)),
                ('imagen', models.ImageField(upload_to='auto_imagenes/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('creado',),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='MarcaModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agencia.modelo')),
            ],
            options={
                'ordering': ('marca',),
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=5000)),
                ('visible', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agencia.auto')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='marca_modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agencia.marcamodelo'),
        ),
        migrations.AddField(
            model_name='auto',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.perfil'),
        ),
        migrations.AddField(
            model_name='auto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
