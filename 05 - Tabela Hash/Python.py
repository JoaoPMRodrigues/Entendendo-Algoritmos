def verifica_valor(tabela, fruta):
    if tabela.get(fruta):
        print(f"O preço da {fruta} é: R${tabela[fruta]:.2f}")
    else:
        print("Não temos tal fruta disponível no momento!")


tabela = {"maçã": 1.5, "pera": 2, "banana": 3.5, "tangerina": 4, "uva": 3}
fruta = "tangerina"
verifica_valor(tabela, fruta)
fruta = "tomate"
verifica_valor(tabela, fruta)
