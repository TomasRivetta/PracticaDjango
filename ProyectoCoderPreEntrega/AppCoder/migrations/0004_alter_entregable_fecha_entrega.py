# Generated by Django 4.1 on 2022-08-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_entregable_entregado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='fecha_entrega',
            field=models.DateField(),
        ),
    ]
