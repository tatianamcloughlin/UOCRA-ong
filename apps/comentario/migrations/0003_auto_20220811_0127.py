# Generated by Django 3.2.5 on 2022-08-11 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20220811_0127'),
        ('comentario', '0002_remove_comentarios_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.noticias')),
            ],
        ),
        migrations.DeleteModel(
            name='Comentarios',
        ),
    ]
