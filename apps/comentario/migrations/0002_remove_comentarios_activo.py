# Generated by Django 3.2.5 on 2022-07-28 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='activo',
        ),
    ]
