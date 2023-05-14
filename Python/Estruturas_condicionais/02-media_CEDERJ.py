input('Importante: informe valores decimais separados por ponto. Tecle ENTER para prosseguir.')

nome = input('Informe seu nome: ')
ad1 = float( input('Informe a nota da AD1: ') )
ap1 = float( input('Informe a nota da AP1: ') )

n1 = round((0.2 * ad1 + 0.8 * ap1), 2)

pergunta_ad2 = input('Se possui nota da AD2, digite 1, caso contrário digite 0. ')

if pergunta_ad2 == '0':
    precisa_n2 = round( (12 - n1), 2)
    print(f'{nome}, sua média em N1 é {n1}')
    print(f'Você precisa ficar com média {precisa_n2} na próxima avaliação para ser aprovado(a)')
else:
    ad2 = float( input('Informe a nota da AD2: '))
    pergunta_ap2 = input('Se possui nota da AP2, digite 1, caso contrário digite 0. ')

    if pergunta_ap2 == '0':
        precisa_ap2 = round( (12 - n1 - 0.2 * ad2/2), 2)
        print(f'{nome}, sua média em N1 é {n1}')
        print(f'Você precisa tirar {precisa_ap2} na AP2 para ser aprovado(a)')
    else:
        ap2 = float( input('Informe a nota da AP2: ') )
        n2 = round( ((0.2 * ad2 + 0.8 * ap2)), 2)
        media_final = (n1 + n2)/2

        if media_final < 6:
            if n1 > n2:
                precisa_ap3 = (10 - n1)/2
                print(f'{nome}, infelizmente você ainda não foi aprovado(a). Sua média final é {media_final}.')
                print(f'Você precisa tirar {precisa_ap3} na AP3 para ser aprovado(a).')
            else:
                precisa_ap3 = (10 - n2)/2
                print(f'{nome}, infelizmente você ainda não foi aprovado(a). Sua média final é {media_final}.')
                print(f'Você precisa tirar {precisa_ap3} na AP3 para ser aprovado(a).')
        else:
           print(f'{nome}, você foi aprovado(a) com média {media_final}')
