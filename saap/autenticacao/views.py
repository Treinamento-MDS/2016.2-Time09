# coding=utf-8
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import RequestContext
from autenticacao.models import Ticket
from autenticacao.models import Usuario_saap, Cidadao, OrganizadorContatos
from django.utils.translation import ugettext
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)

# Create your views here.


def checar_autenticacao(request, resposta_autenticado, resposta_nao_autenticado):
    if request.user.is_authenticated():
        resposta = render(request, resposta_autenticado)
    else:
        resposta = render(request, resposta_nao_autenticado)
    return resposta


def checar_confirmacao(atributo, confirmacao_atributo):
    if atributo == confirmacao_atributo:
        return atributo

def resposta_vazio (request,nao_vazio):
    if nao_vazio == False:
        messages.error(request, 'Preencha todos os campos')
        nao_vazio = redirect('cadastro')
    return nao_vazio

def checar_vazio(campos):
    nao_vazio = True
    for campo in campos:
        if campo == "":
            nao_vazio=False
    return nao_vazio


class LoginView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        resposta = checar_autenticacao(request, 'perfil.html', 'login.html')
        return resposta

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                try:
                    tipo_usuario = Cidadao.objects.get(username=username)
                except:
                    tipo_usuario = None
                if tipo_usuario.__class__ is Cidadao:
                    return render(request, 'perfil.html')

                try:
                    tipo_usuario = OrganizadorContatos.objects.get(username=username)
                except:
                    tipo_usuario = None
                if tipo_usuario.__class__ is OrganizadorContatos:
                    return redirect('/OrganizadorContatos')

            else:
                messages.error(request, 'Conta desativada!')
        else:
            messages.success(request, 'Nome de usuário e/ou senha inválido(s)!')

        return render(request, 'login.html')


class RegistroView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        if request.path == '/cadastro/':
            resposta = checar_autenticacao(request, 'perfil.html', 'cadastro.html')
        elif request.path == '/criar_organizador/':
            resposta = render(request, 'criar_organizador.html')
        return resposta

    def post(self, request):

        first_name = ""
        last_name = ""
        username = ""
        email = ""
        confirmacao_email = ""
        password = ""
        confirmacao_password = ""
        sexo =  ""
        municipio = ""
        uf = ""
        data_de_nascimento = ""

        campos = [request.POST['first_name'], request.POST['last_name'], \
            request.POST['username'], request.POST['email'], \
            request.POST['confirmacao_email'], request.POST['password'], \
            request.POST['confirmacao_password'], request.POST['sexo'], \
            request.POST['municipio'], request.POST['uf'], \
            request.POST['data_de_nascimento']]

        #nao_vazio = checar_vazio(campos)
        #resposta_vazio(request,nao_vazio)


        if checar_vazio(campos):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = checar_confirmacao(request.POST['email'], request.POST['confirmacao_email'])
            password = checar_confirmacao(request.POST['password'], request.POST['confirmacao_password'])
            data_de_nascimento = request.POST['data_de_nascimento']
            sexo = request.POST['sexo']
            municipio = request.POST['municipio']
            uf = request.POST['uf']

            if Cidadao.get_usuario_por_username(username).count() == 0 and \
                OrganizadorContatos.get_usuario_por_username(username).count() == 0:
                email= request.POST['email']
                confirmacao_email =  request.POST['confirmacao_email']

                if email!= confirmacao_email:
                    messages.error(request, 'Emails fornecidos não conferem')
                    response = redirect('cadastro')
                    return response

                password = request.POST['password']
                confirmacao_password = request.POST['confirmacao_password']

                if password!= confirmacao_password:
                    messages.error(request, 'Senhas fornecidas não conferem')
                    response = redirect('cadastro')
                    return response

                if len(password)<6:
                    messages.error(request, 'Utilize ao menos 6 caracteres para senhas')
                    response = redirect('cadastro')
                    return response

                if request.path == '/cadastro/':
                    user = Cidadao()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.username = username
                    user.email = email
                    user.set_password(password)
                    user.data_de_nascimento = data_de_nascimento
                    user.sexo = sexo
                    user.municipio = municipio
                    user.uf = uf
                    user.save()
                    login(request, user)
                    response = render(request, 'perfil.html')
                else:
                    user = OrganizadorContatos()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.username = username
                    user.email = email
                    user.set_password(password)
                    user.data_de_nascimento = data_de_nascimento
                    user.sexo = sexo
                    user.municipio = municipio
                    user.uf = uf
                    user.save()
                    response = render(request, 'login.html')
            else:
                messages.error(request, 'Usuário já cadastrado.')
                response = render(request, 'cadastro')

        else:
            messages.error(request, 'Preencha todos os campos.')
            response = redirect('cadastro')

        return response

class PerfilView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        resposta = checar_autenticacao(request, 'perfil.html', 'login.html')
        return resposta

class LogoutView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        logout(request)
        response = render(request, 'login.html')
        return response


class TicketView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        if request.user.is_authenticated():
            response = render(request, 'ticket.html')
        else:
            response = render(request, 'login.html')
        return response

    def post(self, request):

        novo_ticket = Ticket()

        # Checking if checkbox is checked
        if request.POST.get('enviar_anonimamente', False):
            anonimo = False
        else:
            anonimo = True

        titulo = request.POST['assunto']
        corpo_texto = request.POST.get('descricao')

        if anonimo is True:
            remetente = None
        else:
            remetente = request.user

        tipo_ticket = request.POST['tipo_mensagem']
        arquivo_upload = None

        # Setting new ticket
        if request.user.is_authenticated() is False:

            response = render(request, 'login.html')
        else:
            novo_ticket.envio_anonimo = anonimo
            novo_ticket.titulo = titulo
            novo_ticket.corpo_texto = corpo_texto
            novo_ticket.remetente = remetente
            novo_ticket.gabinete_destino = None
            novo_ticket.tipo_ticket = tipo_ticket
            novo_ticket.file = arquivo_upload
            novo_ticket.save()

            response = render(request, 'perfil.html')

        return response

#Upload de arquivos
    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        return render_to_response('ticket.html', {'form': form})


class MudarSenhaView(View):
    http_method_names = [u'get',u'post']

    def get(self, request):
        response = render (request, 'mudar_senha.html')
        return response

    def post(self,request):
        user = request.user
        nova_senha = request.POST['nova_senha']
        nova_senha2 = request.POST['confirmacao_nova_senha']

        if nova_senha == nova_senha2:
            user.set_password(nova_senha)
            user.save()
        else:
            messages.error(request, 'As senhas não são iguais! Digite novamente.')
            return render(request, 'mudar_senha.html')

        return render(request, 'perfil.html')

class ExcluirContaView(View):
    http_method_names = [u'get', u'post']

    def get(self, request):
        response = render(request, 'excluir_conta.html')
        return response

    def post(self, request):
        password = request.POST['password']
        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            user.delete()
            messages.success(request, 'Sua conta foi excluída')
            response = render(request, 'login.html')
            return response
        else:
            messages.error(request, 'Senha incorreta')
            return render(request, 'excluir_conta.html')
