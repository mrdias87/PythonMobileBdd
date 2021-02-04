import re
from screen_definitions.elementos_dispositivo_produtos_carrinho import Elementos_Produtos_Carrinho


class Acoes_Produtos_Carrinho(Elementos_Produtos_Carrinho):

    def __init__(self, driver):
        super().__init__(driver)

    def verificar_nome_produto_carrinho(self):
        result = self.textviewer_nome_produto.text
        return result

    def verificar_nome_fornecedor_carrinho(self):
        texto = self.textview_nome_fornecedor.text
        nome = re.findall('\\bRoyal Canin\\b', texto, re.IGNORECASE)
        result = nome[0]
        return result

    def verificar_valor_produto_carrinho(self):
        result = self.textviewer_preco_produto.text
        return result
