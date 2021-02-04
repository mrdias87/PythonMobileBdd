from pytest_bdd import *

from screen_actions.acoes_dispositivo_realizar_pesquisa import Acoes_Realizar_Pesquisa
from screen_actions.acoes_dispositivo_comecar_sem_login import Acoes_Comecar_Sem_Login
from screen_actions.acoes_dispositivo_verifica_dados_produto import Acoes_Verifica_Dados_Produto
from screen_actions.acoes_dispositivo_seleciona_produto import Acoes_Seleciona_Produto
from screen_actions.acoes_dispositivo_menu_pesquisa import Acoes_Menu_Navegacao
from screen_actions.acoes_dispositivo_ir_carrinho import Acoes_Ir_Carrinho
from screen_actions.acoes_dispositivo_produtos_carrinho import Acoes_Produtos_Carrinho


@scenario('../features/pesquisa_petz.feature', "Realizar a pesquisa do produto no app")
def test_pesquisapetz():
    pass


@given("que não quero realizar o login")
def sem_login(android_up_drive):
    clica_comecar_sem_login = Acoes_Comecar_Sem_Login(android_up_drive)
    clica_comecar_sem_login.clicar_comecar_sem_login()


@when("clico no botão de pesquisa")
def ativar_pesquisa(android_up_drive):
    clicar_no_botao_pesquisa_menu = Acoes_Menu_Navegacao(android_up_drive)
    clicar_no_botao_pesquisa_menu.clicar_botao_menu_pesquisa()


@when("digito o produto a ser pesquisado")
def digitar_pesquisa(android_up_drive):
    preenche_pesquisa_produto = Acoes_Realizar_Pesquisa(android_up_drive)
    preenche_pesquisa_produto.escreve_pesquisa_produto('Ração')


@when("clico no produto para seleciona-lo")
def selecionar_produto(android_up_drive):
    clicar_produto_menu = Acoes_Seleciona_Produto(android_up_drive)
    clicar_produto_menu.clicar_produto_menu()


@when("verifico se os dados dele estão corretos")
def verificar_dados(android_up_drive):
    verifica_dados_produto = Acoes_Verifica_Dados_Produto(android_up_drive)
    assert verifica_dados_produto.verificar_texto_nome_produto() == 'Ração Royal Canin 15kg Maxi Junior Cães ' \
                                                                    'Filhotes de Raças Grandes '
    assert verifica_dados_produto.verificar_texto_nome_fornecedor() == 'Royal Canin'
    assert verifica_dados_produto.verificar_texto_valor_produto() == '248,89'
    assert verifica_dados_produto.verificar_texto_valor_assinante() == 'R$ 224,00'


@when("adiciono ele ao carrinho")
def adicionar_carrinho(android_up_drive):
    verifica_dados_produto = Acoes_Verifica_Dados_Produto(android_up_drive)
    clicar_no_botao_ir_para_carrinho = Acoes_Ir_Carrinho(android_up_drive)
    verifica_dados_produto.clicar_adicionar_ao_carrinho()
    clicar_no_botao_ir_para_carrinho.clicar_ir_carrinho()


@then("verifico se o produto esta correto no carrinho")
def verifica_carrinho(android_up_drive):
    verifica_produtos_carrinho = Acoes_Produtos_Carrinho(android_up_drive)
    assert verifica_produtos_carrinho.verificar_texto_nome_produto() == 'Ração Royal Canin 15kg Maxi Junior Cães ' \
                                                                        'Filhotes de Raças Grandes '
    assert verifica_produtos_carrinho.verificar_texto_nome_fornecedor() == 'Royal Canin'
    assert verifica_produtos_carrinho.verificar_texto_valor_produto() == '248,89'
    assert verifica_produtos_carrinho.verificar_texto_valor_assinante() == 'R$ 224,00'
