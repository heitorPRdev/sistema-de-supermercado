# Generated by Django 5.0.7 on 2024-07-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='cod_barras',
            field=models.IntegerField(verbose_name='Codego De Barras'),
        ),
    ]
