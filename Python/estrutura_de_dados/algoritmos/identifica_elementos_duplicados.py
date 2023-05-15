# Algoritmo para identificar se há elementos duplicados em uma lista - Comportamento de Algoritmos II

def elementos_duplicados(lista):          # define a função que vai identificar se há elementos duplicados em uma lista
    for i in range(len(lista)-1):         # percorre a lista da posição inicial até a penúltima posição
        for j in range(i+1, len(lista)):  # percorre a lista da posição seguinte até sua última posição
            if lista[i] == lista[j]:      # compara as posições ao percorrer a lista
                return True               # retorna verdadeiro se os elemntos comparados forem iguais (elementos duplicados)
    return False                          # retorna falso quando os elementos comparados são diferentes
# complexidade de espaço: 2 + N
# complexidade de tempo: 

# Rascunho cálculo da complexidade de tempo
# Exemplo de entrada: "PYTHON"
# Quando i = 0 j será = 1 >> executa N-1 operações
# Quando i = 1 j será = 2 >> executa N-2 operações
# Quando i = 2 j será = 3 >> executa N-3 operações
# Quando i = 3 j será = 4 >> executa N-4 operações
# Quando i = 4 j será = 5 >> executa N-5 operações, ou seja, 1 operação
# N-1 + N-2 + N-3 + ... + 1 >> PROGRESSÃO ARITMÉTICA (P.A), então temos que:
# N-1 + N-2 + N-3 + ... + 1 = N*(N-1)/2 + 1 >> (N² - N)/2 + 1 = O(N²)
# >> Ao passo que N cresce, podemos descartar N  e a divisão por 2 e considerar N² como termo dominante

