# -*- coding: utf-8 -*-
from aloe import step, world
import aloe_webdriver
from contextlib import contextmanager

import aloe_webdriver
import aloe_webdriver.django
from aloe import around, world, step
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from autenticacao.models import Cidadao
from time import sleep

@around.each_example
@contextmanager
def with_browser(scenario,outline,steps):
    world.browser = webdriver.Chrome()
    yield
    world.browser.quit()

@step(r'A user is registered')
def register(scenario):
    c = Cidadao()
    c.first_name = 'test_name'
    c.last_name = 'test_last'
    c.username = 'test_name'
    c.email = 'test@email.com'
    c.set_password('123456')
    c.data_de_nascimento = '1990-10-10'
    c.sexo = 'Mascclino'
    c.municipio = 'Brasilia'
    c.uf = 'DF'
    c.save()

@step(r'A gabinete adm is registered')
def registerAdmGabinete(scenario):
    adm = AdministradorGabinete()
    adm.first_name = 'test_name2'
    adm.last_name = 'test_last2'
    adm.username = 'test_name2'
    adm.email = 'test@email.com2'
    adm.set_password('123456')
    adm.data_de_nascimento = '1990-10-10'
    adm.sexo = 'Mascclino'
    adm.municipio = 'Brasilia'
    adm.uf = 'DF'
    gab = Gabinete()
    gab.nome_gabinete = 'gabtest'
    gab.telefone_gabinete = '123456'
    gab.endereco_gabinete = 'rua x'
    gab.cidade_gabinete = 'bsb mesmo'
    gab.cep_gabinete = '1234566'
    gab.save()
    adm.gabinete = gab
    adm.save()

@step(r'Eu seleciono "(.*)" de "(.*)"')
def select(scenario, text, select_id):
    world.browser.find_element_by_xpath("//div[@class='select-wrapper']/select[@id='%s']/../input[@class='select-dropdown']" % select_id).click()
    world.browser.find_element_by_xpath("//li[span[contains(text(),'%s')]]" % text).click()



@step(r'A gabinete is created')
def registerGab(scenario):
    gab = Gabinete()
    gab.nome_gabinete = 'gabtest'
    gab.telefone_gabinete = '123456'
    gab.endereco_gabinete = 'rua x'
    gab.cidade_gabinete = 'bsb mesmo'
    gab.cep_gabinete = '1234566'
    #registerAdm(scenario,gab)
    gab.save()

@step(r'I click in "(.*)"')
def click(scenario, link):
  world.browser.find_element_by_link_text(link).click()


@step(r'Eu seleciono "(.*)" de "(.*)"')
def select(scenario, text, select_id):
    world.browser.find_element_by_xpath("//div[@class='select-wrapper']/select[@id='%s']/../input[@class='select-dropdown']" % select_id).click()
    world.browser.find_element_by_xpath("//li[span[contains(text(),'%s')]]" % text).click()

@step(r'The window is maximized')
def maximize(scenario):
	world.browser.maximize_window()

@step(r'Na topbar eu escolho "(.*)" de "(.*)"')
def select(scenario, text, select_id):
	world.browser.find_element_by_xpath("//a[contains(@class, '%s')]" % select_id).click()
	world.browser.find_element_by_xpath("//li[a[contains(text(),'%s')]]" % text).click()

@step(r'I access "(.*)"')
def access_url(step,url):
    world.fb = url

@step(r'Given I am on SAAP cadastro page')
def given_i_am_on_saap_cadastro_page(step):
    full_url = django.django_url('cadastro')
    world.browser.get(full_url)

@step(u'And I type "([^"]*)" in the field "([^"]*)"')
def and_i_type_group1_in_the_field_group2(step, group1, group2):
    assert False, 'This step must be implemented'

@step(u'And I press "([^"]*)"')
def and_i_press_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'And I choose "([^"]*)"')
def and_i_choose_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'When I press "([^"]*)"')
def when_i_press_group1(step, group1):
    assert False, 'This step must be implemented'

#@step(u'Then I should see "([^"]*)"')
#def then_i_should_see_group1(step, group1):
#    assert False, 'This step must be implemented'
