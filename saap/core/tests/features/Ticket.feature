Feature: Manter tickets

Scenario: Ticket Valido
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "Incidente" de "tipo_mensagem"
		Then I fill in "Assunto" with "tickettest"
		Then Eu seleciono "gabtest" de "nome_gabinete"
		Then I fill in "Mensagem" with "tickettest"
		Then I press "Enviar"
		When I visit site page "/logout"
		When I visit site page "/login"
        Then I fill in "username" with "test_name2"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
        Then I press "Tickets"
        Then I should see "tickettest"

Scenario: Ticket Inválido (sem Gabinete)
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "Incidente" de "tipo_mensagem"
		Then I fill in "Assunto" with "tickettest"
		Then I fill in "Mensagem" with "tickettest"
		Then I press "Enviar"
        Then I should see "O campo Nome do Gabinete não foi preenchido!"

Scenario: Ticket Inválido (sem Tipo de Ticket)
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "gabtest" de "nome_gabinete"
		Then I fill in "Assunto" with "tickettest"
		Then I fill in "Mensagem" with "tickettest"
		Then I press "Enviar"
        Then I should see "O campo Tipo de Ticket não foi preenchido!"

Scenario: Ticket Inválido (sem Assunto)
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "Incidente" de "tipo_mensagem"
		Then I fill in "Mensagem" with "tickettest"
		Then Eu seleciono "gabtest" de "nome_gabinete"
		Then I press "Enviar"
        Then I should see "O campo Assunto não foi preenchido!"

Scenario: Ticket Inválido (sem Mensagem)
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "Incidente" de "tipo_mensagem"
		Then I fill in "Assunto" with "tickettest"
		Then Eu seleciono "gabtest" de "nome_gabinete"
		Then I fill in "Assunto" with "tickettest"
		Then I press "Enviar"
        Then I should see "O campo Mensagem não foi preenchido!"

Scenario: Deletar Ticket
        Given A user is registered
		And The window is maximized
		And A gabinete adm is registered	
        When I visit site page "/login"
        Then I fill in "username" with "test_name"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
		Then Na topbar eu escolho "Ticket" de "dropdown-button"
		Then Eu seleciono "Incidente" de "tipo_mensagem"
		Then I fill in "Assunto" with "tickettest"
		Then Eu seleciono "gabtest" de "nome_gabinete"
		Then I fill in "Mensagem" with "tickettest"
		Then I press "Enviar"
		When I visit site page "/logout"
		When I visit site page "/login"
        Then I fill in "username" with "test_name2"
        Then I fill in "password" with "123456"
        Then I press "Enviar"
        Then I press "Tickets"
		When I visit site page "/deletar_ticket/1"
        Then I should not see "tickettest"

