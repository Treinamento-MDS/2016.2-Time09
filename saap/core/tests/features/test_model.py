from core.models import Ticket, Carta
import pytest
from django.test import Client
from autenticacao.models import OrganizadorContatos

"""@pytest.mark.django_db
def test_public_view_ticket():
    c = Client()
    organizador = OrganizadorContatos()

    organizador.username = 'organizador'
    organizador.first_name = 'contato'
    organizador.data_de_nascimento = '2016-10-15'
    organizador.username = 'organizador'
    organizador.email = 'organizador@email.com'
    organizador.set_password('123456')
    organizador.sexo = 'masculino'
    organizador.municipio = 'Brasilia'
    organizador.uf = 'DF'

    organizador.save()

    c.login(username='organizador',password='123456')

    response= {'envio_anonimo': 'Anonimo',
              'enviar_anonimamente': 'True',
              'descricao': 'Rua com burracos',
              'assunto':'blablabla',
              'tipo_mensagem':'oioioioioi',
              'nome_organizador':"contato"}

    c.post('/ticket/', response)

    ticket = Ticket.objects.all()[0]
    response= {'ticket_id': ticket.id}

    retorno = c.post('/publicar_ticket/', response,follow=True)

    assert retorno.status_code == 200
"""
@pytest.mark.django_db
def test_model_carta():

    carta = Carta()

    carta.nome_remetente = 'nome_teste1'
    carta.nome_destinatario = 'nome_teste2'
    carta.data = '2016-10-23'
    carta.local = 'local_teste'
    carta.assunto = 'assunto_teste'
    carta.texto = 'texto_teste'

    carta.save()
    cartas = Carta.objects.all().count()

    assert cartas >= 1
    carta.delete()
