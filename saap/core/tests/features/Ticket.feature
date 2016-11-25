Feature: Login de Usuário

Scenario: Ticket Valido
        Given A gabinete adm is registered
        When I visit site page "/login"
        Then I fill in "username" with "test_name2"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
        Then I should see "Olá test_name, seja bem vindo ao Sistema de Apoio à Atividade Parlamentar!"