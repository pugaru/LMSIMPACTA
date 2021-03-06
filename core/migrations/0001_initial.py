# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:08
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=50)),
                ('ra', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('perfil', models.CharField(default='C', max_length=1)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('carga_horaria', models.IntegerField(default=1000)),
                ('periodo', models.CharField(default='Noturno', max_length=20)),
                ('ativo', models.BooleanField(default=True)),
                ('descricao', models.TextField(blank=True)),
                ('Matriz_Curricular', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Texto', models.TextField()),
                ('Data_Publicada', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('apelido', models.CharField(max_length=15)),
                ('carga_horaria', models.IntegerField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disciplina')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.usuario',),
        ),
    ]
