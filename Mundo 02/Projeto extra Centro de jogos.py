#PROJETO EXTRA --------------------------------------------------------------------------------
from time import sleep

cor = {'vermelho':'\33[31m',
       'verde':'\33[32m',
       'azul':'\33[34m',
       'limpa':'\33[m'}

print('==' * 16)
texto = 'SEJA BEM-VINDO!'
print(f'{cor['azul']}{texto:^33}')
print(f'JOGUE NOSSOS JOGOS E DIVIRTA-SE!{cor['limpa']}')
print('==' * 16)

print(f'''{cor['azul']}[ 1 ] Adivinhação
[ 2 ] Pedra, papel e tesoura
[ 3 ] Ímpar ou par
[ 4 ] Tabuada
[ 5 ] Pensamento
[ 0 ] SAIR{cor['limpa']}''')
opcao = int(input(f'{cor['vermelho']}Selecione o jogo que deseja jogar: {cor['limpa']}'))

print('\n')
print(f'{cor['verde']}PROCESSANDO...{cor['limpa']}')
sleep(1.0)
print('\n')

if opcao == 1:
    print('Você escolheu: ADIVINHAÇÃO! \n')

    from random import randint
    computador = randint(1, 10)
    vitorias = 0

    while True:
        print('Tente adivinhar o número!')
        jogador = int(input(f'{cor['verde']}Digite um número de 1 a 10: {cor['limpa']}'))
        if jogador == computador:
            print(f'{cor['azul']}Você VENCEU. Parabéns! :){cor['limpa']} \n')
            vitorias += 1

        if jogador != computador:
            print(f'{cor['vermelho']}Você PERDEU. Infelizmente! :({cor['limpa']} \n')
            print(f'Você teve uma sequência de {vitorias} vitória(s). \n')
            continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if continuar == 'S':
                continue
            if continuar == 'N':
                print(f'{cor['azul']}Fim dos jogos, obrigado por participar! :){cor['limpa']}')
                break

if opcao == 2:
    print('Você escolheu: PEDRA, PAPEL E TESOURA \n')
    lista = ['Pedra', 'Papel', 'Tesoura']
    from random import randint
    computador = randint(0, 2)
    vitorias = 0
    empate = 0

    while True:
        print(f'''{cor['azul']}[0] PEDRA
[1] PAPEL
[2] TESOURA{cor['limpa']}''')
        jogador = int(input(f'{cor['verde']}O que você joga: {cor['limpa']}'))

        print('\n')
        print(f'{cor['vermelho']}JOKENPO000...{cor['limpa']} \n')
        sleep(0.5)

        if lista[computador].upper().capitalize() == lista[jogador].upper().capitalize():
            print(f'{cor['verde']}EMPATEEE!!{cor['limpa']}')

        elif (jogador == 0 and computador == 2) or \
            (jogador == 1 and computador == 0) or \
            (jogador == 2 and computador == 1):
            print(f'{cor['azul']}Você VENCEU. Parabéns! :){cor['limpa']} \n')
            vitorias += 1
        else:
            print(f'{cor['vermelho']}Você PERDEU. Infelizmente! :({cor['limpa']} \n')
            print(f'Você teve uma sequência de {vitorias} vitória(s). \n')
            continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if continuar == 'S':
                continue
            if continuar == 'N':
                print(f'{cor['azul']}Fim dos jogos, obrigado por participar! :){cor['limpa']}')
                break

if opcao == 3:
    print('Você escolheu: ÍMPAR OU PAR \n')
    contagem = 0
    while True:
        jogador = int(input('Me diga o número: '))
        from random import randint
        computador = randint(0, 10)
        total = jogador + computador
        tipo = ' '

        while tipo not in 'PI':
            tipo = str(input('PAR ou ÍMPAR? [P/I]: ')).upper().strip()[0]
        print(f'Você jogou: {jogador} e o computador jogou: {computador}. Dando um total de: {total} \n')

        if tipo == 'P':
            if total % 2 == 0:
                print('Você VENCEU!')
                contagem += 1
            else:
                print('Você PERDEU!')
                break

        elif tipo == 'I':
            if total % 2 == 0:
                print('Você VENCEU!')
                contagem += 1
            else:
                print('Você PERDEU!')
                break
        print('Vamos jogar novamente... \n')
    print(f'GAME OVER!!! Você venceu {contagem} vezes.')

if opcao == 4:
    print('Você escolheu: TABUADA \n')

    print('Caso queira encerrar o programa, digite: -1')

    tabuado = 0
    while True:
        numero = int(input('''Quer ver a tabuada de qual número? 
Digite um número: '''))
        print('\n')

        if numero == -1:
            print('Tabuada finalizada! Volte sempre. :)')
            break

        for c in range(1, 11):
            mult = numero * c
            print(f'{numero} x {c} = {mult}')
        print('\n')

if opcao == 5:
    print('Você escolheu: PENSAMENTO \n')

    print('''Sou uma máquina pensante...
E acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? (O.o)\n''')
    from random import randint

    tentativas = 0
    aleatorio = randint(1, 10)
    while True:
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1

        if aleatorio > palpite:
            print('MAIS... Tente novamente!')

        elif aleatorio < palpite:
            print('MENOS... Tente novamente!')

        elif aleatorio == palpite:
            print(f'\nPARABÉNS, Você acertou!!! Usando {tentativas} tentativa(s).')
            break

    print('FIM!')

if opcao == 0:
    print(f'{cor['azul']}OBRIGADO POR JOGAR! :D {cor['limpa']} \n')
