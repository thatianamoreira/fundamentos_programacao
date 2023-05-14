# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code
# Questão 8
# Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
# Dica: Use três variáveis:
# ● um contador;
# ● uma variável para soma;
# ● e uma variável para os termos.
# Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3

soma_termos = 0
inverso_fatorial = 0

for i in range(1, 1001):
    if i == 1:
        inverso_fatorial = 1/i
        print('----------------------------------------')
        print(f'i = {i}')
        print(f'Inverso fatorial = {inverso_fatorial}')
        print(f'Soma termos = {soma_termos}')
    else:
        inverso_fatorial = 1/(i * (i-1))
    soma_termos += inverso_fatorial
    ('----------------------------------------')
    print(f'i = {i}')
    print(f'Inverso fatorial = {inverso_fatorial}')
    print(f'Soma termos = {soma_termos}')
print(soma_termos)