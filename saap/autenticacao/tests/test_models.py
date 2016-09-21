# coding=utf-8
from autenticacao.models import Usuario_saap
import pytest
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

# def test_deleta_usuario():
#     u = Usuario_saap()
#     u.first_name = 'test_name'
#     u.last_name = 'test_last'
#     u.username = 'test_name'
#     u.email = 'test@email.com'
#     u.set_password('123')
#     u.data_de_nascimento = '1990-10-10'
#     u.sexo = 'Masculino'
#     u.municipio = 'Brasilia'
#     u.uf = 'DF'
#     u.save()

#     users_test = Usuario_saap.objects.filter(first_name__startswith=u.first_name)
#     assert u in users_test
#     u.delete()
