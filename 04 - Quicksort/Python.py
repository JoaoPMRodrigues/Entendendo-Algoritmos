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


minha_lista = [2, 1, 3, 7, 4, 9, 6, 10, 0, 5]
print(quicksort(minha_lista))
