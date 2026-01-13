from collections import deque

def pessoa_vendedor(nome):
    """Verifica se o nome termina com a letra 'm'."""
    return nome[-1] == "m"

def verificar_nome():
    """Verifica na fila se há um vendedor de manga."""
    fila = deque()
    grafo = dict()
    grafo["voce"] = ["alice", "bob", "claire"]
    grafo["bob"] = ["anuj", "peggy"]
    grafo["alice"] = ["peggy"]
    grafo["claire"] = ["thom", "jonny"]             
    grafo["anuj"] = []
    grafo["peggy"] = []
    grafo["thom"] = []
    grafo["jonny"] = []
    fila += grafo["voce"]
    while fila:
        pessoa=fila.popleft()
        if pessoa_vendedor(pessoa):
            return print(f"{pessoa} é um(a) vendedor(a) de manga!")
        else:
            fila += grafo[pessoa]
    return print("Nenhum vendedor de manga encontrado.")

if __name__ == "__main__":
    verificar_nome()
 