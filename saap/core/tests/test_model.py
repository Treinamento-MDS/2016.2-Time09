#coding=utf-8

import pytest
from django.test import Client
from core.models import Grupo


@pytest.mark.django_db
def test_grupo_Creation():
	
	before = Grupo.objects.all().count()

	grupo = Grupo()
	grupo.nome = 'brasileiros'
	grupo.save()

	after = Grupo.objects.all().count()	

	assert before < after

@pytest.mark.django_db
def test_str_method():

	grupo = Grupo()
	grupo.nome = "Brasileiros"

	grupo.save()

	assert "Brasileiros" is grupo.__str__()
