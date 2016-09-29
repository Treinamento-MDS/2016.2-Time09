# coding=utf-8
from autenticacao.views import *
import pytest
from django.test import Client
from autenticacao.models import Usuario_saap, Cidadao


@pytest.mark.django_db
def test_login_view_post_false():

    client = Client()
    username = 'teste'
    password = 'teste'
    assert client.login(username=username, password=password) is False


@pytest.mark.django_db
def test_login_view_get():

    client = Client()
    response = client.get('/login/')
    assert response.status_code is 200


def test_checar_vazio_true():

    variaveis = ['teste']
    assert checar_vazio(variaveis)


def test_checar_vazio_false():

    variaveis = ['']
    assert checar_vazio(variaveis) is False


def test_checar_confirmacao():
    assert checar_confirmacao('teste', 'teste')


def test_registro_view_get():

    client = Client()
    response = client.get('/cadastro/')
    assert response.status_code is 200


@pytest.mark.django_db
def test_registro_cidadao_valido():

    client = Client()
    before = len(Cidadao.objects.all())

    client.post('/cadastro/', {'first_name': 'test_name',
                               'last_name': 'test_last',
                               'username': 'test_name',
                               'email': 'test@email.com',
                               'confirmacao_email': 'test@email.com',
                               'password': '123456',
                               'confirmacao_password': '123456',
                               'data_de_nascimento': '1990-10-10',
                               'sexo': 'Masculino',
                               'municipio': 'Brasilia',
                               'uf': 'DF'})

    after = len(Cidadao.objects.all())

    assert after > before
    Cidadao.objects.get(username='test_name').delete()
