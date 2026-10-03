#2° MUNDO
#Aula 12
#Condições aninhadas - Estruturas de controle

# se = if: / se não se = elif: / se não = else:
#Você pode criar varios blocos com 'elif:', não precisa ser somente 03 possibilidades
#Não se pode usar 'elif:' sem 'if:' mas se pode usar infinitos 'elif:' dentro de um 'if:'
#Ex. 58 Vendo em um código
from time import sleep
cores = {'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'limpa':'\033[m'}
nome = str(input('Qual o seu nome? ')).strip()
print(f'{cores['vermelho']}PROCESSANDO...{cores['limpa']}')
sleep(0.5)
print(f'{cores['vermelho']}.')
sleep(0.3)
print('..')
sleep(0.3)
print(f'...{cores['limpa']}')
sleep(0.5)
if nome == 'Mayezer':
    print('Seu nome é muito bonito!!')
elif nome == 'Jorge' or nome == 'Maria' or nome == 'José' or nome == 'Ana' or nome == 'Paulo':
    print('Seu nome é muito comum no Brasil!')
elif nome in 'Mayender Elino Iran':
    print('Seu nome é masculino!')
elif nome in 'Samara Regina Tati':
    print('Seu nome é feminino!')
else:
    print('Seu nome é bem normal!')
print(f'{cores['azul']}--{cores['limpa']}' * 14)
print(f'Tenha um ótimo dia {cores['azul']}{nome}{cores['limpa']}!')
print(f'{cores['azul']}--{cores['limpa']}' * 14)

#Ex. 59 Atividade 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
cores = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'limpa':'\033[m'}
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
print(f'{cores['verde']}PROCESSANDO...{cores['limpa']}')
sleep(1.5)
print('\n')
divisao = casa / (anos * 12)
porcentagem = salario * 0.30
if divisao <= porcentagem:
    print(f'Para pagar uma casa de: R${casa:.2f}, em {anos:.0f} anos a prestação será de R${divisao:.2f}')
    print(f'Empréstimo {cores['azul']}APROVADO!!!{cores['limpa']}')
else:
    print(f'Para pagar uma casa de: R${casa:.2f}, em {anos:.0f} anos a prestação será de R${divisao:.2f}')
    print(f'Empréstimo {cores['vermelho']}NEGADO!!!{cores['limpa']}')

#Ex. 60 Atividade 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
cores = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpa':'\033[m'}
inteiro = int(input('Digite um número inteiro: '))
binario = bin(inteiro)
octal = oct(inteiro)
hexadecimal = hex(inteiro)
print('Escolha uma das bases para conversão:')
print('[ 01 ] converter para BINÁRIO')
print('[ 02 ] converter para OCTAL')
print('[ 03 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
print(f'{cores['verde']}PROCESSANDO...{cores['limpa']}')
sleep(1.5)
print('\n')
if opcao == 1:
    print(f'{inteiro} convertido para BINARIO é igual a: {binario[2:]}')
elif opcao == 2:
    print(f'{inteiro} convertido para OCTAL é igual a: {octal[2:]}')
elif opcao == 3:
    print(f'{inteiro} convertido pata HEXADECIMAL é igual a: {hexadecimal[2:]}')
else:
    print(f'{cores['vermelho']}Opção invalida, tente novamente!!{cores['limpa']}')

#Ex. 61 Atividade 38: Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior e Não existe valor maior, os dois são iguais.
from time import sleep
color = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpa':'\033[m'}
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(f'{color['verde']}PROCESSANDOOOOOO...{color['limpa']}')
sleep(1)
print('\n')
if numero1 > numero2:
    print(f'O primeiro número é maior, sendo assim. O número: {numero1} é maior que o número: {numero2}')
elif numero1 < numero2:
    print(f'O Segundo número é maior, sendo assim. O número: {numero2} é maior que o número: {numero1}')
else:
    print(f'{color['vermelho']}Os números são iguais!{color['limpa']}')

#Ex. 62 Atividade 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
atual = int(2025)
ano = int(input('Ano de nascimento: '))
idade = atual - ano
calculo1 = 18 - idade
calculo2 = idade - 18
if idade < 18:
    print('Você ainda está muito novo para o alistamento!')
    print(f'Você tem: {idade} anos.')
    print(f'Volte em: {calculo1} anos.')
elif idade == 18:
    print(f'Você tem: {idade} anos.')
    print('Você está no ano EXATO para se alistar!')
else:
    print(f'Você tem: {idade} anos.')
    print(f'Você deveria ter se alistado a: {calculo2} anos.')
    print('Você precisará pagar uma multa, você passou da idade de alistamento!')

#Ex. 63 Atividade 40: Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO e Média 7.0 ou superior: APROVADO.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Com a média de: {media:.2f} | Você foi REPROVADO!')
elif 6.9 > media >= 5.0:
    print(f'Com a média de: {media:.2f} | Você está de RECUPERAÇÃO!')
else:
    print(f'Com a média de: {media:.2f} | Você está APROVADO!')

#Ex. 64 Atividade 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
from time import sleep
cor = {'vermelhor':'\033[31m',
       'verde':'\033[32m',
       'limpa':'\033[m'}
ano = int(input('Qual a sua idade? '))
print(f'{cor['verde']}PROCESSADO...{cor['limpa']}')
sleep(1.5)
if ano <= 9:
    print(f'Você tem {ano} anos, por tanto está na categoria MIRIM!')
elif 9 < ano <= 14:
    print(f'Você tem {ano} anos, por tanto está na categoria INFANTIL!')
elif 14 < ano <= 19:
    print(f'Você tem {ano} anos, por tanto está na categoria JÚNIOR!')
elif 19 < ano <= 25:
    print(f'Você tem {ano} anos, por tanto está na categoria SÊNIOR!')
else:
    print(f'Você tem {ano} anos, por tanto está na categoria MÁSTER!')

#Ex. 65 Atividade 42: Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente e ESCALENO: todos os lados diferentes.
segmento1 = int(input('Digite o PRIMEIRO segmento: '))
segmento2 = int(input('Digite o SEGUNDO segmento: '))
segmento3 = int(input('Digite o TERCEIRO segmento: '))
if segmento1 == segmento2 == segmento3:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif segmento1 >= segmento2 <= segmento3 or segmento1 <= segmento2 >= segmento3:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
elif segmento1 >= segmento2 >= segmento3 or segmento1 <= segmento2 <= segmento3:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

#Ex. 66 Atividade 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
peso = int(input('Qual o seu peso? (kg): '))
altura = float(input('Qual a sua altura? (m): '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'Com um IMC de {imc:.1f}, você está ABAIXO do peso!')
    print('')
elif 18.6 >= imc <= 25:
    print(f'Com um IMC de {imc:.1f}, você está no peso IDEAL!')
    print('PARABÉNS!!!')
elif 25.1 >= imc <= 30:
    print(f'Com um IMC de {imc:.1f}, você está com SOBREPESO!')
    print('Bom!!')
elif 30.1 >= imc <= 40:
    print(f'Com um IMC de {imc:.1f}, você está com OBESIDADE!')
    print('Cuidado, cuide bem da sua vida!')
else:
    print(f'Com um IMC de {imc:.1f}, você está com OBESIDADE MÓRBIDA!')
    print('Agite a sua vida, URGENTE!')

#Ex. 67 Atividade 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
from time import sleep
print('----- LOJA XINGU -----')
print('\n')
preco = float(input('Preço final da compra: R$'))
print('\n')
print('FORMAS DE PAGAMENTO')
print('[ 1 ] Á vista: PIX ou DINHEIRO')
print('[ 2 ] Á vista: CARTÃO DE DÉBITO')
print('[ 3 ] 2x no CARTÃO DE CRÉDITO')
print('[ 4 ] 3x ou + no CARTÃO DE CRÉDITO')
print ('\n')
escolha = int(input('Digite a opção de pagamento: '))
print('\n')
print('PROCESSANDO...')
sleep(1.0)
print('\n')
op1 = preco - (preco * 0.10)
op2 = preco - (preco * 0.05)
op3 = preco + (preco * 0.20)

if escolha == 1:
    print(f'Sua compra de R${preco:.2f} vai custar R${op1:.2f} no total!')
elif escolha == 2:
    print(f'Sua compra de R${preco:.2f} vai custar R${op2:.2f} no total!')
elif escolha == 3:
    print(f'Sua compra terá o valor total de R${preco:.2f}')
elif escolha == 4:
    parcelas = int(input('Quantas parcelas: '))
    op4 = op3 / parcelas
    print(f'Sua compra de R${preco:.2f}, será dividido em {parcelas}x custando R${op4:.2f} cada parcela. \nCustando R${op3:.2f} no total!')
else:
    print('OPÇÃO INVALIDA!')

#Ex. 68 Atividade 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
while True:
    cor = {'nvermelho':'\033[1:31m',
           'nverde':'\033[1:32m',
           'limpa':'\033[m'}
    print(f'{cor['nvermelho']}=-=-' * 5)
    print('Vamos jogar JOKENPO!')
    print(f'=-=-' * 5)
    print(f'{cor['limpa']}')
    print('Suas opções:')
    print(f'{cor['nverde']}[ 0 ] PEDRA')
    print('[ 1 ] PAPEL')
    print(f'[ 2 ] TESOURA{cor['limpa']}')
    jogador = int(input('Qual a sua jogada? '))
    print(f'{cor['nvermelho']}JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)
    print(f'\n{cor['limpa']}')
    print('-=-' * 9)
    print(f'Computador jogou: {cor['nverde']}{lista[computador].lower().capitalize()}{cor['limpa']} \nJogador jogou: {cor['nverde']}{lista[jogador].lower().capitalize()}{cor['limpa']}')
    print('-=-' * 9)
    print('\n')
    if jogador < 0 or jogador > 2:
        print(f'{cor['nvermelho']}JOGADA INVALIDA!{cor['limpa']}')
        print('Jogue novamente!')
    elif lista[computador].lower().capitalize() == lista[jogador].lower().capitalize():
        print('EMPATE! :)')
        print('\n')
        teste0 = input('Deseje parar? (sim/não): ').strip().lower()
        if teste0 == 'sim'.strip().lower():
            if teste0.startswith('s'):
                print(f'{cor['nverde']}Obrigado por jogar! :){cor['limpa']}')
                break
        else:
            print('\n')
            print('Vamos jogar novamente! :)')
            print('\n')
    elif (jogador == 0 and computador == 2) or \
            (jogador == 1 and computador == 0) or \
            (jogador == 2 and computador == 1):
        print('Você VENCEU!!!! :)')
        print('\n')
        teste1 = input('Deseje parar? (sim/não): ').strip().lower()
        if teste1 == 'sim'.strip().lower():
            if teste1.startswith('s'):
                print(f'{cor['nverde']}Obrigado por jogar! :){cor['limpa']}')
                break
        else:
            print('\n')
            print('Vamos jogar novamente! :)')
            print('\n')
    else:
        print(f'{cor['nvermelho']}Você PERDEU! :({cor['limpa']}')
        print('\n')
        teste2 = input('Deseje parar? (sim/não): ').strip().lower()
        if teste2 == 'sim'.strip().lower():
            if teste2.startswith('s'):
                print(f'{cor['nverde']}Obrigado por jogar! :){cor['limpa']}')
                break
        else:
            print('\n')
            print('Vamos jogar novamente! :)')
    print('\n')