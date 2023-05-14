# Calcula e exibe a média final do(a) aluno(a) e se foi aprovado(a) ou não;
# Se aluno(a) não foi aprovado(a), calcula e exibe o valor que deve tirar na prova de recuperação;


soma_notas = 0

nome = input('Informe o nome do(a) aluno(a): ')

for posicao in range(1, 5):
    nota = float( input(f'Informe a nota {posicao}: '))
    soma_notas = soma_notas + nota
media = soma_notas/posicao

if media >= 7:
    print(f'Parabéns, {nome}, você foi aprovado(a) com média {media}')
elif media >= 5:
    precisa_recuperacao = 14 - media
    print(f'{nome}, sua média é {media}.')
    print(f'Você está em recuperação e precisa obter {precisa_recuperacao} para ser aprovado(a).')
else:
    print(f'{nome}, você foi reprovado(a) com média {media}.')