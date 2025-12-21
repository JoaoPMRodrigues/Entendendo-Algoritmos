def buscaMenor(arr):
    """Essa fução calcula o
    menor valor da função e 
    retorna o seu índice"""
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaiporSelecao(arr):
    """Esta função ordena um array do seu menor ao 
    maior valor pelo método de ordenação por seleção"""
    novoArr = list()
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


meu_arr = [5, 2, 3, 4, 0, 1]
print(ordenacaiporSelecao(meu_arr))
