# Generated by Django 3.2.5 on 2022-07-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField(null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]