Feature: Manter tickets

Scenario: Ticket Valido
		Given A user is registered
        Given A gabinete adm is registered
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
        Then I should see "Olá test_name, seja bem vindo ao Sistema de Apoio à Atividade Parlamentar!"


Scenario: Ticket Invalido
        Given A user is registered
		And The window is maximized	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
        Then Na topbar eu escolho "Ticket" de "dropdown-button"
        #Then I should see "efwefwef"
        Then Eu seleciono "Ticket" de "dropdown1"
