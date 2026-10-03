#Aula 10
#Condições simples e compostas

#if (Se for)
#else (Se NÃO for)
# se = if: / se não se = elif: / se não = else:

#Ex. 46 Extrutura de condição ou acontece um ou outro.
#if carro.esquerda();
    #bloco True
#else:
    #bloco False

#Ex. 47 Testando
tempo = int(input('Quantos anos tem seu carro? '))
print('\n')
if tempo <= 3:
    print('Carro Novo!')
else:
    print('Carro Velho!')

print('--FIM!--')

#Ex. 48 Atividade 28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
while True:
    from random import randint
    from time import sleep
    from color50 import rgb, constants
    computador = randint(0, 5)
    color0 = rgb(100, 0, 250)
    color1 = rgb(200, 50, 200)
    color2 = rgb(50,200,250)
    color3 = rgb(100, 250, 100)
    color4 = rgb(250, 100, 0)
    print(color0 + '-=-' * 19 + constants.RESET)
    print(color2 + 'Vou pensar em um número entre 0 a 5. Tente adivinhar...' + constants.RESET  )
    print(color0 + '-=-' * 19 + constants.RESET)
    numero = int(input('Em que número eu pensei? '))
    print('\n')
    print(color1 + 'PROCESSANDO... :O' + constants.RESET)
    sleep(2)
    if numero == computador:
        print(color4 + 'UAU!!! Parabéns, você acertou!!! :D' + constants.RESET)
        break
    else:
        print(color3 + f'Infelizmente, você errou. Pensei no número: {computador} \nTente novamente! :>' + constants.RESET)
    print('\n')

#Ex. 49 Atividade 29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from color50 import rgb, constants
color0 = rgb(100, 180, 80)
color1 = rgb(100, 180, 80)
color2 = rgb(200, 80, 80)
velocidade = float(input(color0 + 'Qual a velocidade atual do carro? ' + constants.RESET))
if velocidade <= 80:
    print(color1 + 'Tenha um ótimo dia. Dirija com responsabilidade!' + constants.RESET)
else:
    multa = (velocidade - 80) * 7
    print(color2 + f'MULTADO! Você excedeu o limite de velocidade permitido que é: 80Km/h \nVocê deve pagar uma multa de: R${multa:.2f} \nDirija com segurança!' + constants.RESET)

#Ex. 50 Atividade 30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')

#Ex. 51 Atividade 31 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
from color50 import rgb, constants
color0 = rgb(100, 50, 50)

print(color0 + '-=-' * 23 + constants.RESET)
print('Estamos com uma promoção para viagens mais longas, APROVEITE!!"')
print(color0 + '-=-' * 23 + constants.RESET)
print('\n')
km = int(input('Qual a distância da sua viagem? (KM): '))
print('\n')
soma0 = km * 0.50
soma1 = km * 0.45
if km <= 200:
    print(f'A sua viagem de {km}km terá o valor de R$ {soma0:.2f}')
else:
    print(f'A sua viagem de {km}km terá o valor de R$ {soma1:.2f}')

#Ex. 52 Atividade 32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
from color50 import rgb, constants
color0 = rgb(200, 0, 20)
print(color0 + 'Coloque 0 para analisar o ano atual!' + constants.RESET)
ano = int(input('Qua ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')

#Ex. 53 Atividade 33 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep
from color50 import rgb, constants
color0 = rgb(200, 50 ,100)
n0 = int(input('Primeiro número: '))
n1 = int(input('Segundo número: '))
n2 = int(input('Terceiro número: '))
lista = [n0, n1, n2]
print(color0 + '\nPROCESSANDO... \n... \n' + constants.RESET)
sleep(1.5)
print(f'O MENOR número é: {min(lista)}')
print(f'O MAIOR número é: {max(lista)}')
#Ou--------------------------------------------------------------------uO#
from time import sleep
from color50 import rgb, constants
color0 = rgb(200, 50 ,100)
n0 = int(input('Primeiro número: '))
n1 = int(input('Segundo número: '))
n2 = int(input('Terceiro número: '))
lista = [n0, n1, n2]
print(color0 + '\nPROCESSANDO... \n... \n' + constants.RESET)
sleep(1.5)
menor = n0
if n1<n0 and n1<n2:
    menor = n1
if n2<n0 and n2<n1:
    menor = n2
maior = n1
if n1>n0 and n1>n2:
    maior = n1
if n2>n0 and n2>n1:
    maior = n2
print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')

#Ex. 54 Atividade 34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? R$'))
calculo0 = (salario * 0.10) + salario
calculo1 = (salario * 0.15) + salario
if salario >= 1250.00:
    print(f'Seu salário é de: R${salario:.2f}, você tem um aumento de 10%, que fica: R${calculo0:.2f}')
else:
    print(f'Seu salário é de: R${salario:.2f}, você tem um aumento de 15%, que fica: R${calculo1:.2f}')

#Ex. 55 Atividade 35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n0 = float(input('Primeiro segmento: '))
n1 = float(input('Segundo segmento: '))
n2 = float(input('Terceiro segmento: '))
if n0 < n1 + n2 and n1 < n0 + n2 and n2 < n0 + n1:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')