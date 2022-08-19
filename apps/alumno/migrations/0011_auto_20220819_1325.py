# Generated by Django 3.2.5 on 2022-08-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0010_myuser_contra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='contra',
        ),
        migrations.AddField(
            model_name='myuser',
            name='ciudad',
            field=models.CharField(max_length=100, null=True, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='cuil',
            field=models.IntegerField(max_length=20, null=True, verbose_name='Cuil'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='provincia',
            field=models.CharField(max_length=100, null=True, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='dni',
            field=models.IntegerField(max_length=20, null=True, verbose_name='DNI'),
        ),
    ]