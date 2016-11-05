# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import *
from core.models import Contato, Ticket, Carta

class Usuario_saap(User):

    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=10)
    municipio = models.CharField(max_length=250)
    uf = models.CharField(max_length=2)

    @classmethod
    def busca_nome(cls, nome):
        return Usuario_saap.objects.filter(first_name__startswith=nome)

    @classmethod
    def deleta_usuario(cls, idArg):
        Usuario_saap.objects.get(id=idArg).delete()

    @classmethod
    def busca_username(cls, username):
        return Usuario_saap.objects.filter(username__startswith=username)

    @classmethod
    def get_usuario_por_username(cls, username):
        return Usuario_saap.objects.filter(username=username)

class Cidadao(Usuario_saap):

    pass

class OrganizadorContatos(Usuario_saap):

    pass

class Gabinete(models.Model):

    # parlamentar = models.ForeignKey(AdministradorGabinete, \
    #                                 on_delete=models.CASCADE)
    organizadores_contatos = models.ManyToManyField(OrganizadorContatos)
    # organizadores_agenda = models.ManyToManyField(OrganizadorAgenda)
    contatos = models.ManyToManyField(Contato)
    tickets = models.ManyToManyField(Ticket)
    cartas = models.ManyToManyField(Carta)
    endereco_gabinete = models.CharField(max_length=100)
