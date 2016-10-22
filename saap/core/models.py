# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import *
# from autenticacao.models import Gabinete_saap
# from autenticacao.models import Usuario_saap
from saap import *
# from autenticacao.models import

class Grupo(models.Model):

    nome = models.CharField(max_length=30)
    contatos = models.ManyToManyField('Contato',related_name='grupo')

    def __str__(self):
        return self.nome

    @classmethod
    def filtro_nascimento(cls,mes_do_ano):
        return  cls.objects.filter(contatos__data_de_nascimento__contains=mes_do_ano)

    @classmethod
    def filtro_cidade(cls,cidade):
        return cls.objects.filter(contatos__cidade__contains=cidade)

    @classmethod
    def filtro_genero(cls,sexo):
        return cls.objects.filter(contatos__sexo=sexo)

class Contato(models.Model):

    nome = models.CharField(max_length=60,default='')
    data_de_nascimento = models.DateField('')
    sexo = models.CharField(max_length=10,default='')
    endereco = models.CharField(max_length=60,default='')
    cidade = models.CharField(max_length=20,default='')
    cep = models.CharField(max_length=8,default='')
    estado = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=30,default='')
    telefone = models.CharField(max_length=7,default='',blank=True,null=True)
    celular = models.CharField(max_length=8,default='',blank=True,null=True)
    fax = models.CharField(max_length=8,default='',blank=True,null=True)
    cpf = models.CharField(max_length=15,default='',blank=True,null=True)
    rg= models.CharField(max_length=13,default='',blank=True,null=True)
    titulo = models.CharField(max_length=30,default='',blank=True,null=True)
    titulo_de_eleitor = models.CharField(max_length=30,default='',blank=True,null=True)
    zona = models.CharField(max_length=30,default='',blank=True,null=True)
    secao = models.CharField(max_length=30,default='',blank=True,null=True)
    profissao = models.CharField(max_length=30,default='',blank=True,null=True)
    cargo = models.CharField(max_length=30,default='',blank=True,null=True)
    empresa = models.CharField(max_length=30,default='',blank=True,null=True)
    dependente_nome = models.CharField(max_length=30,default='',blank=True,null=True)
    dependente_aniversario = models.CharField(max_length=30,default='',blank=True,null=True)
    dependente_parentesco = models.CharField(max_length=30,default='',blank=True,null=True)
    dependente_partido = models.CharField(max_length=30,default='',blank=True,null=True)
    dependente_data_filiacao = models.DateField('',blank=True,null=True)

class Ticket(models.Model):

    envio_identificado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100)
    corpo_texto = models.CharField(max_length=500)
    remetente = models.CharField(max_length=250)
    # gabinete_destino = Gabinete_saap()
    data_publicacao = models.DateField('data_de_publicacao', auto_now=True)
    tipo_ticket = models.CharField(max_length=30)
    aprovado = models.BooleanField(default=False)

