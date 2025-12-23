def quicksort(array):
    """Ordenação simples de uma 
    lista a partir do quicksort"""
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


def mergesort(lista, inicio=0, fim=None):
    """Ordenação simples de uma
    lista a partir do mergesort"""
    if fim == None:
        fim = len(lista)

    if ((fim-inicio) > 1):
        meio = (inicio+fim)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    return lista


def merge(lista, inicio, meio, fim):
    """Divide a lista ao meio e 
    reconecta as ordenando"""
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0
    for k in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[k] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[k] = direita[topo_direita]
            topo_direita += 1


minha_lista = [2, 1, 3, 7, 4, 9, 6, 10, 0, 5]
print(quicksort(minha_lista))
print(mergesort(minha_lista))
