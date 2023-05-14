# Código que solicita que o(a) usuário(a) informe seu nome e idade, verifica se usuário(a) é maior ou menor
# de idade e imprime o nome do(a) usuário(a) e se ele(a) é maior ou menor de idade"""

nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

if idade < 18:
    print(f'{nome}, você é menor de idade.')
else:
    print(f'{nome}, você é maior de idade.')