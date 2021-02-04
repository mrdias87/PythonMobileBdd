Feature: Pesquisa de Produto
  Eu como usuário,
  quero realizar uma pesquisa de um produto,
  para poder realizar a compra dele no aplicativo.

  Scenario: Realizar a pesquisa do produto no app
    Given que não quero realizar o login
     When clico no botão de pesquisa
      And digito o produto a ser pesquisado
      And clico no produto para seleciona-lo
      And verifico se os dados dele estão corretos
      And adiciono ele ao carrinho
     Then verifico se o produto esta correto no carrinho