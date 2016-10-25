# coding=utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (CadastroView, DeletarContatoView, ContatoView, TicketView,
                    AtualizaContato, GabinetesView, PublicarTicketView,
                    DeletarTicketView, GerarCartaView, CartasView,
                    BuscaContatosView, CriarGrupoDeContatosView,
                    AdicionarContatoAoGrupo, OficioView,DeletarOficioView, 
                    GerarOficioView, GerarPDFOficioView, EnviarOficioView,
                    GabineteView, TicketsView,
                    DeletarCartaView, GerarPDFCartaView, EnviarCartaView,
                    BuscaContatosView, CriarGrupoDeContatosView)

urlpatterns = [
    url(r'^cadastro_contato/$', login_required(CadastroView.as_view()),
        name='cadastro_contato'),
    url(r'^exclui_contato/$', login_required(DeletarContatoView.as_view()),
        name='exclui_contato'),
    url(r'^gabinete/contatos/$', login_required(ContatoView.as_view()),
        name='contatos'),
    url(r'^atualiza_contato/$', login_required(AtualizaContato.as_view()),
        name='atualiza_contato'),
    url(r'^ticket/$', TicketView.as_view(),
        name='ticket'),
    url(r'^publicar_ticket/$', PublicarTicketView.as_view(),
        name='publicar_ticket'),
    url(r'^deletar_ticket/(?P<pk>[0-9]+)/$', DeletarTicketView.as_view(),
        name='deletar_ticket'),
    url(r'^gabinetes/$', GabinetesView.as_view(),
        name='gabinetes'),
    url(r'^gabinete/cartas/gerar_carta/$', login_required(GerarCartaView.as_view()),
        name='gerar_carta'),
    url(r'^gabinete/cartas/$', login_required(CartasView.as_view()),
        name='cartas'),
    url(r'^deletar_carta/(?P<pk>[0-9]+)/$', login_required(DeletarCartaView.as_view()),
        name='deletar_carta'),
    url(r'^gerar_pdf/(?P<pk>[0-9]+)/$', login_required(GerarPDFCartaView.as_view()),
        name='gerar_pdf'),
    url(r'^enviar_carta/(?P<pk>[0-9]+)/$', login_required(EnviarCartaView.as_view()),
        name='enviar_carta'),
<<<<<<< HEAD
    url(r'^criar_grupo/$', CriarGrupoDeContatosView.as_view(),
        name='criar_grupo'),
    url(r'^busca_contatos/$', BuscaContatosView.as_view(),
        name='busca_contatos'),
    url(r'^adicionar_contatos/$', AdicionarContatoAoGrupo.as_view(),
        name='adicionar_contatos'),
    url(r'^grupo_contatos/$', GrupoDeContatosView.as_view(),
        name='grupo_contatos'),
    url(r'^criar_grupo/$', CriarGrupoDeContatosView.as_view(),
        name='criar_grupo'),
    url(r'^gerar_oficio/$', GerarOficioView.as_view()),
    url(r'^gabinete/oficios/gerar_oficio/$', GerarOficioView.as_view(),
        name = 'gerar_oficio'),
    url(r'^deletar_oficio/(?P<pk>[0-9]+)/$', DeletarOficioView.as_view(),
        name='deletar_oficio'),
    url(r'^gerar_oficio_pdf/(?P<pk>[0-9]+)/$', login_required(GerarPDFOficioView.as_view()),
        name='gerar_oficio_pdf'),
    url(r'^enviar_oficio/(?P<pk>[0-9]+)/$', login_required(EnviarOficioView.as_view()),
        name='enviar_oficio'),
    url(r'^gabinete/oficios/$', login_required(OficioView.as_view()),
        name='oficios'),
    url(r'^gabinete/$', login_required(GabineteView.as_view()),
        name='gabinete'),
    url(r'^gabinete/tickets/$', login_required(TicketsView.as_view()),
        name='tickets'),
    url(r'^grupo_contatos/$', GrupoDeContatosView.as_view(),
        name='grupo_contatos'),
    url(r'^criar_grupo/$', CriarGrupoDeContatosView.as_view(),
        name='criar_grupo'),
     url(r'^busca_contatos/$', BuscaContatosView.as_view(),
        name='busca_contatos'),
]
