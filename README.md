# Entendendo Algoritmos

Este repositório contém estudos pessoais e anotações autorais
baseados na minha leitura do livro "Entendendo Algoritmos"
(Grokking Algorithms), de Aditya Y. Bhargava.

O conteúdo aqui apresentado é uma interpretação própria,
produzida como forma de aprendizado, e não substitui
a leitura da obra original.

## 1. Introdução

### O que eu entendi: 

* Algoritmos são uma sequência de passos para resolver um problema
* O mesmo problema pode ser resolvido com um número diferente de passos
* O tempo de Execução de um algoritmo é definido pela Notação Big O
* Alguns dos tempos de execução do mais rápido ao mais lento são (Em Bio O):

1. O(Log(n))
2. O(N)
3. O(N*Log(n))
4. O(N²)
5. O(N!)

* Pesquisa Binária (O(log(N))) é mais rápida que Pesquisa Simples (N)

### O que eu não entendi:

* Como analisar a complexidade de um algoritmo
* Acredito que esteja tudo bem, pois não parece ser a proposta do livro ensinar isso

## 2. Ordenação por Seleção

### O que eu entendi: 

* Memória funciona como várias gavetas dentro de um armário
* Arrays e Listas são usados para guardas vários dados juntos
* Nos Arrays os dados são guardados um do lado do outro
* Nas Listas Encadeadas os dados são guardados separados
* Nas listas Encadeadas um dado guarda o endereço do próximo
* Ordenação por Seleção tem o tempo de Execução de O(N²)
* Tabela de comparação do tempo de execução:

BIG O | Arrays | Listas
---|---|---
Leitura | O(1) | O(N)
Inserção | O(N) | O(1)
Eliminção | (ON) | O(1)


## Recursão

### O que eu entendi: 

* Recursão  é uma técnica onde uma função chama a si mesma
* Nem sempre vai ser mais rápida que a solução usando loops
* Torna a resolução muito mais simples, mesmo sem ganho de velocidade
* Pilhas funcionam como uma pilha de pratos, você põe ou tira os pratos de cima da pilha
* O normal é usar função recursiva (na execução) e pilha (na memória) ao mesmo tempo
* Se o código ficar muito grande, pode dar Stack Overflow (Estourar a memória)
* Tome cuidado com loops infinitos na função, tenha sempre um caso base

### O que eu não entendi:

* No começo eu tive dificuldade em entender como funciona o gerenciamento de memória nas pilhas
* Mas, conforme avança o capítulo e com uns exemplos, isso fica mais fácil de entender
