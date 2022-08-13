# Generated by Django 3.2.5 on 2022-08-13 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='imagen1',
            new_name='imagen',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='imagen2',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='imagen3',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='imagen4',
        ),
        migrations.AddField(
            model_name='cursos',
            name='logo',
            field=models.ImageField(null=True, upload_to='cursos/'),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='cursos/')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos')),
            ],
        ),
    ]
