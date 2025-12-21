def PesquisaBinaria(lista, item):
    """Implementação simples de busca binária.
    Retorna o índice do item, se encontrado."""

    baixo = 0
    alto = len(lista)-1
    total_passos = 0
    while baixo <= alto:
        meio = (baixo+alto)//2
        chute = lista[meio]
        total_passos += 1
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 3, 5, 7, 9]
print(PesquisaBinaria(minha_lista, 3))
