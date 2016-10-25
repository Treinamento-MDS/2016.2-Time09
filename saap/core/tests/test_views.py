# coding=utf-8
from core.views import *
from autenticacao.models import OrganizadorContatos
import pytest
from django.test import Client
from core.models import Ticket
from autenticacao.models import OrganizadorContatos


@pytest.mark.django_db
def test_enviar_ticket():
    client = Client()

    organizador = OrganizadorContatos()
    
    organizador.username = 'sabino'
    organizador.first_name = 'sabino'
    organizador.data_de_nascimento = '1990-01-01'
    organizador.sexo = 'masculino'
    organizador.municipio = 'ceilandia'
    organizador.uf = 'df'
    organizador.set_password('eusoueu0')

    organizador.save()



    user = client.login(username='sabino', password='eusoueu0')

    request = {
    "nome_organizador":"sabino",
    "enviar_anonimamente":"False",
    "assunto" : "blablabla",
    "descricao" : "corpo_texto",
    "envio_anonimo": "anonimo",
    "tipo_mensagem": "blablabla"
    }

    response = client.post('/ticket/',request)
    tickets = Ticket.objects.all().count()

    assert tickets == 1
    Ticket.objects.all()[0].delete()


@pytest.mark.django_db
def test_deletar_ticket():
    client = Client()

    organizador = OrganizadorContatos()
    
    organizador.username = 'sabino'
    organizador.first_name = 'sabino'
    organizador.data_de_nascimento = '1990-01-01'
    organizador.sexo = 'masculino'
    organizador.municipio = 'ceilandia'
    organizador.uf = 'df'
    organizador.set_password('eusoueu0')

    organizador.save()

    client.login(username='sabino', password='eusoueu0')

    request = {
    "nome_organizador":"sabino",
    "enviar_anonimamente":"False",
    "assunto" : "blablabla",
    "descricao" : "corpo_texto",
    "envio_anonimo": "anonimo",
    "tipo_mensagem": "blablabla"
    }

    client.post('/ticket/',request)

    tickets_before = Ticket.objects.all().count()
    
    ticket = Ticket.objects.all().last()

    client.get('/deletar_ticket/'+str(ticket.id),follow=True)
    
    tickets_after = Ticket.objects.all().count()
    assert tickets_before > tickets_after

@pytest.mark.django_db
def test_vereadores_view_get():

	client = Client()
	response = client.get('/vereadores/')
	assert response.status_code is 200

@pytest.mark.django_db
def test_vereadores_view_post_nao_existe():

	client = Client()
	response = client.post('/vereadores/', {'nome_organizador': ''})
	assert response.status_code is 200

@pytest.mark.django_db
def test_vereadores_view_post_existe():

	organizador = OrganizadorContatos()
	organizador.first_name = 'Organizador'
	organizador.data_de_nascimento = '1900-01-01'
	organizador.save()
	client = Client()
	response = client.post('/vereadores/', {'nome_organizador': 'Organizador'})
	assert response.status_code is 200
	organizador.delete()

@pytest.mark.django_db
def test_busca_contatos_cidade():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Taguatinga'
    contato.cep = '72000000'
    contato.estado = 'DF'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "cidade"
    pesquisa = 'df'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()


@pytest.mark.django_db
def test_busca_contatos_estado():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "estado"
    pesquisa = 'Sao Paulo'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()

@pytest.mark.django_db
def test_busca_contatos_genero():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "genero"
    pesquisa = 'Masculino'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()

@pytest.mark.django_db
def test_busca_contatos_data_aniversario():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "data_de_nascimento"
    pesquisa = '1'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()

@pytest.mark.django_db
def test_busca_contatos_data_aniversario():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "Data_aniversario"
    pesquisa = '1'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()

@pytest.mark.django_db
def test_busca_contatos_nome():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = "nome"
    pesquisa = 'Maria'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete()  

@pytest.mark.django_db
def test_busca_contatos_sem_filtro():

    contato = Contato() 
    contato.nome = 'teste'
    contato.data_de_nascimento='1990-01-01'
    contato.sexo = 'Masculino'
    contato.endereco = 'Qnl 29 teste casa teste 20'
    contato.cidade = 'Osasco'
    contato.cep = '72000000'
    contato.estado = 'Sao Paulo'
    contato.email = "teste@teste.com"
    contato.save()


    client = Client()
    tipo_busca = ""
    pesquisa = 'sabino'
    response = client.post('/busca_contatos/',{'tipo_busca':tipo_busca,'pesquisa':pesquisa})

    assert response.status_code == 200
    contato.delete() 

@pytest.mark.django_db
def test_criar_grupo_de_contatos():

    client=Client()

    banco_antes = Grupo.objects.all().count()
    teste_nome_grupo = 'brasileiros'

    client.post('/criar_grupo/',{'nome_grupo':teste_nome_grupo})

    banco_depois = Grupo.objects.all().count()

    assert banco_depois > banco_antes
    Grupo.objects.all().last().delete()


