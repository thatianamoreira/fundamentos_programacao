# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code

# Questão 1 (adaptada)
# Faça um programa que peça ao usuário um número e imprima todos os
# números pares de um até o número que o usuário informar, inclusive.

contador = 0
numero_digitado = int( (input('Digite um número inteiro: ')))

for contador in range(contador, numero_digitado+1, 2):
    print(contador)