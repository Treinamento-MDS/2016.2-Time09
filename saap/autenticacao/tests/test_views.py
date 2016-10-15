# coding=utf-8
from autenticacao.views import *
from autenticacao.models import *
import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

@pytest.fixture
def logar_usuario(client):
	user = User(username="asdf",password="1234")
	user.set_password('123456')
	user.save()
	client.login(username=user.username, password="123456")
	return user,client

@pytest.mark.django_db
def teste_usuario_logado(client):
	user,client = logar_usuario(client)

	assert user is not None

@pytest.mark.django_db
def test_login_view_get(client):
	response = client.get('/login/')
	assert 300 >= response.status_code < 400

def test_registro_view_get():
	client = Client()
	response = client.get('/cadastro/')
	assert response.status_code is 200

def test_checar_vazio_true():

	variaveis = ['teste']
	assert checar_vazio(variaveis)

def test_checar_vazio_false():

	variaveis = ['']
	assert checar_vazio(variaveis) is False

def test_checar_confirmacao():
	return checar_confirmacao('teste','teste')

def test_registro_view_get():
	client = Client()
	response = client.get('/cadastro/')
	assert response.status_code is 200

@pytest.mark.django_db
def test_registro_view_get_login():

	client = Client()
	client.login(username='test',password='test')
	response = client.get('/cadastro/')
	assert response.status_code is 200

@pytest.mark.django_db
def test_tipo_usuario_cidadao():

	cidadao = Cidadao()
	cidadao.username = 'cidadao'
	cidadao.set_password('123')
	cidadao.data_de_nascimento = '1900-01-01'
	cidadao.save()
	client = Client()
	response = client.post('/', {'username': 'cidadao', 'password': '123'})
	assert response.status_code is 200
	cidadao.delete()

@pytest.mark.django_db
def test_tipo_usuario_organizador_contatos():

	organizador = OrganizadorContatos()
	organizador.username = 'organizador'
	organizador.set_password('123')
	organizador.data_de_nascimento = '1900-01-01'
	organizador.save()
	client = Client()
	response = client.post('/', {'username': 'organizador', 'password': '123'})
	assert response.status_code is 200
	organizador.delete()

@pytest.mark.django_db
def test_checar_autenticacao():

	cidadao = Cidadao()
	cidadao.username = 'cidadao'
	cidadao.set_password('123')
	cidadao.data_de_nascimento = '1900-01-01'
	cidadao.save()
	request = Client()
	request.user = authenticate(username='cidadao', password='123')
	autenticacao = checar_autenticacao(request, True, False)
	assert autenticacao == True
	cidadao.delete()

@pytest.mark.django_db
def test_mudar_senha_view_get():

	cidadao = Cidadao()
	cidadao.username = 'cidadao'
	cidadao.set_password('123')
	cidadao.data_de_nascimento = '1900-01-01'
	cidadao.save()
	client = Client()
	request = client.post('/', {'username': 'cidadao', 'password': '123'})
	response = client.get('/mudar_senha/')
	assert response.status_code is 200
	cidadao.delete()
