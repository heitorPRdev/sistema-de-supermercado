from django.db import models

class Produtos(models.Model):
    nome_podu = models.CharField(verbose_name='Nome',max_length=100, null=False , blank=False)
    cod_barras = models.IntegerField(verbose_name='Codego De Barras',null=False , blank=False)
    valid = models.DateField(verbose_name='Validade',max_length=100, null=False , blank=False)
    peso = models.FloatField(verbose_name='Peso',max_length=100, null=False , blank=False)
    fornecedor = models.CharField(verbose_name='Fornecedor',max_length=100, null=False , blank=False)