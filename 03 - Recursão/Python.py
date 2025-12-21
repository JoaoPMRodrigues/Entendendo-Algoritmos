from time import sleep


def contagemRegressiva(i):
    """Faz uma conttagem regressiva básica"""
    if i > 0:
        print(i, end="... ")
        sleep(0.2)
        contagemRegressiva(i-1)
    else:
        return print("Fim!")


contagemRegressiva(10)


def fatorial(n):
    '''Calcula o fatorial de um 
    número usando função recursiva'''
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é: {fatorial(n)}")
