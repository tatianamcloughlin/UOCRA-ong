# Generated by Django 3.2.5 on 2022-08-20 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='cuil',
            field=models.BigIntegerField(null=True, verbose_name='Cuil'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='dni',
            field=models.BigIntegerField(null=True, verbose_name='DNI'),
        ),
    ]
