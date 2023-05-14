# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code

# Questão 4
# Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
# a) o produto entre o dobro do primeiro e a metade do segundo.
# b) a soma entre o triplo do primeiro e o terceiro.
# c) o terceiro elevado ao cubo.

num1 = int( input('Informe um número inteiro: '))
num2 = int( input('Informe outro número: '))
num3 = float( input('Informe um número real: '))

a = 2 * num1 * (num2/2)
b = 3 * num1 + num3
c = num3 ** 3

print(f'2 x {num1} x ({num2}/2) = {a}')
print(f'3 x {num1} + ({num3}) = {b}')
print(f'{num3}^3 = {c}')