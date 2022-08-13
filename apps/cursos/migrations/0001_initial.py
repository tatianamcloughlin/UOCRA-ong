# Generated by Django 3.2.5 on 2022-08-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('duracion', models.CharField(max_length=50, null=True)),
                ('imagen1', models.ImageField(null=True, upload_to='cursos/')),
                ('imagen2', models.ImageField(upload_to='cursos/')),
                ('imagen3', models.ImageField(upload_to='cursos/')),
                ('imagen4', models.ImageField(upload_to='cursos/')),
            ],
        ),
    ]
