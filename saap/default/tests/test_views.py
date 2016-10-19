from autenticacao.views import *
import pytest

def test_checar_vazio_true():
	variaveis = ['teste']
	assert checar_vazio(variaveis)

def test_checar_vazio_false():
	variaveis = ['']
	assert checar_vazio(variaveis) is False
