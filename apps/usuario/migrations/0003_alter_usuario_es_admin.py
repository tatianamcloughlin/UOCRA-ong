# Generated by Django 3.2.5 on 2022-08-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_es_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='es_admin',
            field=models.BooleanField(default=False),
        ),
    ]