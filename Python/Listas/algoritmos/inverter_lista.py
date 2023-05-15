# Algoritmo para inverter lista - Comportamento de Algoritmos I

# divide a lista em duas partes
# primeiro elemento da lista será o último e o último será o primeiro. Enquanto o segundo será o penúltimo e o penúltimo será o segundo e assim por diante.

def inverter_lista(lista):              # define a função que vai inverter a lista
    tamanho = len(lista)                # calula o tamanho da lista e armazena na variável tamanho
    limite = tamanho // 2               # calcula o valor que represenbta a metade do tamanho da lista e armazena na variável limite
    for i in range(limite):             # percorre a primeira metade da lista
        aux = lista[i]                  # armazena o elemento na iésima posição da lista na variável temporária aux
        lista[i] = lista[tamanho - i]   # faz a troca de posição entre os elementos da lista
        lista[tamanho - i] = aux        # reinsere na lista, em nova posição, o elemento armazenado temporariamente na variável aux
# 4 + N valores em memória >> 4 + N  complexidade de espaço (memória)
# 2 + 4 * limite >> 2 + 4 * (N/2) >> 2 + 2N - complexidade de tempo (processamento)


## Outro algoritmo para se inverter uma lista

def inverter_lista2(lista):                        # define a função que vai inverter a lista
    nova_lista = []                                # cria uma nova lista vazia, que será a lista invertida
    tamanho = len(lista)                           # calcula o tamanho da lista e o armazena na variável tamanho
    for i in range(tamanho):                       # percorre a lista
        nova_lista.append(lista[tamanho - i - 1])  # insere os elementos da lista em ordem inversa na nova lista
    return nova_lista                              # retorna a nova lista
# complexidade de espaço: 3 + 2 * N
# complexidade de tempo: 2 + N

## complexidade é uma medida da quantidade de recursos que são demandados por um algoritmo
## complexidade de tempo: calcula a quantidade de processamento que o algoritmo precisa para executar
## complexidade de espaço: calcula a quantidade de memória que o algoritmo precisa para executar