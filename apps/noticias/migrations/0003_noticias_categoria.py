# Generated by Django 3.2.5 on 2022-08-01 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('noticias', '0002_alter_noticias_imagenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categorias'),
        ),
    ]