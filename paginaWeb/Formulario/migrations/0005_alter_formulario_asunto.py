# Generated by Django 4.0.5 on 2022-06-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0004_alter_formulario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='asunto',
            field=models.CharField(max_length=20),
        ),
    ]
