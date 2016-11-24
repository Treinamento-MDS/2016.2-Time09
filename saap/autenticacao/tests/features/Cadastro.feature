Feature: Cadastro de Usuário
  To get acess to the saap features
  As an citizen 
  I want to register my self

Scenario: Cadastro invalido sem sexo
        When I visit site page "/cadastro"
        Then I fill in "first_name" with "user_first"
        Then I fill in "last_name" with "user_last"
        Then I fill in "username" with "user_username"
        Then I fill in "email" with "user_email@email.com"
        Then I fill in "confirmacao_email" with "user_email@email.com"
        Then I fill in "password" with "user_password"
        Then I fill in "confirmacao_password" with "user_password"
        Then I fill in "data_de_nascimento" with "1990-10-10"
        Then I fill in "municipio" with "brasilia"
        Then I press "Enviar"
		Then I should see "O campo Sexo não foi preenchido!"
