# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code
# Questão 7
# Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
# coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do
# segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). Em seguida, calcule a distância
# euclidiana entre os pontos:

x1 = float( input('Informe o valor de x1: '))
y1 = float( input('Informe o valor de y1: '))
x2 = float( input('Informe o valor de x2: '))
y2 = float( input('Informe o valor de y2: '))

distancia_euclidiana = ( (x2 - x1)**2 + (y2 - y1)**2 ) ** (1/2)

print(f'A distância euclidiana entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é {distancia_euclidiana:.2f}')