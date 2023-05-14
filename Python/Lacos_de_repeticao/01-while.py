# Usuário deve tentar advinhar o número secreto, compreendido entre 0 e 50


numero_secreto = 29
numero_tentativas = 1

numero_escolhido = int( input('Informe um número inteiro entre 0 e 50: '))

while numero_escolhido != numero_secreto:
    print(f'{numero_tentativas}ª tentativa >> Você errou! Tente novamente.')
    numero_tentativas += 1
    print()
    numero_escolhido = int( input('Informe um número inteiro entre 0 e 50: ')) 
print(f'Você acertou na {numero_tentativas}ª tentativa! O número secreto é {numero_secreto}')