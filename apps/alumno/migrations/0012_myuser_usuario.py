# Generated by Django 3.2.5 on 2022-08-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0011_auto_20220819_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='usuario',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre usuario'),
        ),
    ]
