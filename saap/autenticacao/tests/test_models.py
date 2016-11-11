# coding=utf-8
from autenticacao.models import Usuario_saap, AdministradorGabinete, Gabinete_saap
import pytest
import tempfile
# Create your tests here.

@pytest.mark.django_db
def test_busca_nome():
    u = Usuario_saap()
    u.first_name = 'test_name'
    u.last_name = 'test_last'
    u.username = 'test_name'
    u.email = 'test@email.com'
    u.set_password('123')
    u.data_de_nascimento = '1990-10-10'
    u.sexo = 'Masculino'
    u.municipio = 'Brasilia'
    u.uf = 'DF'
    u.save()

    users_test = Usuario_saap.busca_nome(u.first_name)
    assert u in users_test
    u.delete()

@pytest.mark.django_db
def test_deleta_usuario():
    u = Usuario_saap()
    u.first_name = 'test_name'
    u.last_name = 'test_last'
    u.username = 'test_name'
    u.email = 'test@email.com'
    u.set_password('123')
    u.data_de_nascimento = '1990-10-10'
    u.sexo = 'Masculino'
    u.municipio = 'Brasilia'
    u.uf = 'DF'
    u.save()
    db_before = Usuario_saap.objects.get(pk=1)

    Usuario_saap.deleta_usuario(1)
    db_after = Usuario_saap.objects.all()
    # db_before.count() > db_after.count()
    assert db_before is not \
    None and db_after.count() is 0

@pytest.mark.django_db
def test_busca_username():

    u = Usuario_saap()
    u.first_name = 'test_name'
    u.last_name = 'test_last'
    u.username = 'test_name'
    u.email = 'test@email.com'
    u.set_password('123')
    u.data_de_nascimento = '1990-10-10'
    u.sexo = 'Masculino'
    u.municipio = 'Brasilia'
    u.uf = 'DF'
    u.save()
    verifica_user = Usuario_saap.busca_username('test_name')

    assert verifica_user.count() > 0
    u.delete()

@pytest.mark.django_db
def test_model_gabinete_saap():

    gabinete = Gabinete_saap()
    u = Usuario_saap()

    u.first_name = 'test_name'
    u.last_name = 'test_last'
    u.username = 'test_name'
    u.email = 'test@email.com'
    u.set_password('123')
    u.data_de_nascimento = '1990-10-10'
    u.sexo = 'Masculino'
    u.municipio = 'Brasilia'
    u.uf = 'DF'
    u.save()

    gabinete.nome_gabinete = 'gabinete'
    gabinete.municipio = 'Brasilia'
    gabinete.uf = 'DF'
    gabinete.enderecoCasa = 'enderecoCasa_teste'
    gabinete.enderecoGabinete = 'enderecoGabinete_teste'
    gabinete.emailCorporativo = 'emailCorporativo@teste.com'
    gabinete.logoCasa = tempfile.NamedTemporaryFile(suffix=".jpg").name
    gabinete.save()

    gabinete.participantes.add(u)

    gabinetes = Gabinete_saap.objects.all().count()
    assert gabinetes >= 1
    gabinete.delete()
    u.delete()
