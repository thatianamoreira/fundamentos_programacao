# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code

# Questão 3
# Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
# área desse círculo. Lembrando que a área de círculo é dada pela equação: A = ℼ r^2.

import math

def area_circulo(raio):
    return math.pi * (raio**2)
    
raio = float( input('Qual é o valor do raio do círculo? '))
area = round( area_circulo(raio), 4)

print(f'A área do círculo de rario {raio} é {area}')