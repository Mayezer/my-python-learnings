#Aula 15
#Interrompendo repetições while
#Parte 3 - Laços de repetição

#Fazendo loop com while True:
#Com o comando - break - Para o loop infinito

#Ex.
soma = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    if n == 1000:
        break
soma -= 1000
print(f'{soma}')
#--------------------------------------------
n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 1000:
        break
    soma += n
print(f'{soma}')

#O que é pep - Python Enhancement Proposal - Que em português significa Proposta de Melhoria para Python.

#Ex. Atividade 66
from time import sleep
n = soma = quant = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    quant += 1
print('PROCESANDO...')
sleep(1.0)
print(f'A soma entre os números é: {soma}')
sleep(0.5)
print(f'Foram digitados {quant} números.')

#Ex. Atividade 67
tabuado = 0
print('''Valor criar um tabuada!?
Caso queira encerrar o programa, digite: -1 \n''')
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

#Ex. Atividade 68
from random import randint
print('+_' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('+_' * 12)
contagem = 0
while True:
    jogador = int(input('Me diga o número: '))
    computador = randint(0, 1000)
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

#Ex. Atividade 69
homem = 0
mais18 = 0
while True:
    print('--' * 10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo | [M/F]: ')).upper().strip()[0]
    print('--' * 10)
    continuar = str(input('Quer CONTINUAR? [S/N]: ')).upper().strip()[0]
    print('\n')
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Obrigado por participar! \n')
        mais18 = idade >= 18
        homem += 1
        print(f'Total de pessoas com mais de 18 anos: {mais18}.')
        print(f'Ao todo temos {homem} homens cadastrados.')
        print(f'E temos  mulheres acima de 20 anos.')
        break
    else:
        print('Opção INVALIDA. Tente novamente!')
#------------------------------------------------------------------------------------------
homem = 0
mulher20 = 0
mais18 = 0
while True:
    print('--' * 10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo | [M/F]: ')).upper().strip()[0]
    print('--' * 10)
    continuar = str(input('Quer CONTINUAR? [S/N]: ')).upper().strip()[0]
    print('\n')
    if sexo == 'M':
        homem += 1
    if idade >= 18:
        mais18 += 1
    if sexo == 'F' and idade >= 20:
        mulher20 += 1
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Obrigado por participar! \n')
        print(f'Total de pessoas com mais de 18 anos: {mais18}.')
        print(f'Ao todo temos {homem} homens cadastrados.')
        print(f'E temos {mulher20} mulheres acima de 20 anos.')
        break
    else:
        print('Opção INVALIDA. Tente novamente!')

#Ex. Atividade 70
total = 0
maisdemil = 0
maisbarato = None
cont = 0
barato = ' '
print('+_' * 8)
print('LOJA GLOBO MIX')
print('+_' * 8)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    total += 1 * preco
    if preco >= 1000:
        maisdemil += 1
    if maisbarato is None or preco < maisbarato:
        maisbarato = preco
        barato = nome
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('\nFIM DO PROGRAMA\n')
        print(f'O total da compra foi de: R${total:.2f}')
        print(f'Temos {maisdemil} produto custando mais de R$1000.00')
        print(f'O produto mais barato foi {barato} que custa: R${maisbarato:.2f}')
        break
    else:
        print('Opção INVÁLIDA. Tente novamente!')

#Ex. Atiidade 71
print('~' * 10)
print('Branco BIO')
print('~' * 10)
print('\n')
dinheiro = int(input('Quanto você deseja sacar? R$'))
n50 = 50
valor50 = dinheiro // n50
resto = dinheiro % 50
valor20 = resto // 20
resto = resto % 20
valor10 = resto // 10
resto = resto % 10
valor1 = resto
if valor50 > 0:
    print(f'Você receberá {int(valor50)} notas de R$50.00')
if valor20 > 0:
    print(f'Você receberá {int(valor20)} notas de R$20.00')
if valor10 > 0:
    print(f'Você receberá {int(valor10)} notas de R$10.00')
if valor1 > 1:
    print(f'Você receberá {int(valor1)} notas de R$1.00')

#Ex. Atividade 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numero0 = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
           'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
           'ONZE','DOZE', 'TREZE', 'CATORZE', 'QUINZE',
           'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    for c in range(0, 20):
        numero1 = int(input('Digite um número entre 0 e 20: '))
        if numero1 <= 20:
            print(f'Você digitou o número: {numero0[numero1]} \n')
            continuar = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
            print('\n')
            if continuar == 'S':
                continue
            elif continuar == 'N':
                print('Obrigado por participar dessa pesquisa!')
                break
        else:
            print('Tente novamente!', end= ' ')
            break
    break
