# Generated by Django 3.2.5 on 2022-08-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_alter_noticias_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]