# Generated by Django 3.2.5 on 2022-08-18 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0006_auto_20220818_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='date_of_birth',
            new_name='fecha',
        ),
    ]