# Generated by Django 5.0.7 on 2024-07-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_podu', models.CharField(max_length=100, verbose_name='Nome')),
                ('cod_barras', models.IntegerField(max_length=100, verbose_name='Codego De Barras')),
                ('valid', models.DateField(max_length=100, verbose_name='Validade')),
                ('peso', models.FloatField(max_length=100, verbose_name='Peso')),
                ('fornecedor', models.CharField(max_length=100, verbose_name='Fornecedor')),
            ],
        ),
    ]
