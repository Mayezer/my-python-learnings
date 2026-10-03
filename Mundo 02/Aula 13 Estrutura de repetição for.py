#Aula 13
#Estrutura de repetição - for
#Estrutura de controle, também conhecidas como: Laços, repetições ou iteração.

#Estrutura de laço - Fica repetindo comandos
#Ex. Vendo em um código
#laço c no intervado(1,10):
#   passo
#pega
#------------------------------------
#for c in range(1,10):
#   passo
#pega
#------------------------------------
#laço c no intervalor(0,3):
#   passo
#   pula
#passo
#pega
#------------------------------------
#for c in range(0,3):
#   passo
#   pula
#passo
#pega
#------------------------------------
#laço c no intervalo(0,3):
#   se tiver moeda:
#       pega
#   passo
#   pula
#passo
#pega
#------------------------------------
#for c in range(0,3):
#   if moeda:
#       pega
#   passo
#   pula
#passo
#pega

#O número 0 conta na hora da contagem de repetições e contagem regressiva.
#E ele ignora a última casa, caso você mande printar (0,6) ele retornará 0,1,2,3,4 e 5.
#Vendo na prática
#Ex.
for c in range(0,6):
    print('Oi')
print('FIM!')
#Aqui ele retornaria(repetiria) 'Oi' 6 vezes por conta do ínicio começar com '0'.
#Caso fosse: (1, 6) ele retornaria(repetiria) o 'Oi' 5 vezes.

#Ex. Para fazer uma contagem de trás para frente, ficaria:
for c in range(6, 0, -1):
    print(c)
print('FIM!')
#Aqui ele retornaria(contaria): 6, 5, 4, 3, 2, 1 / FIM!

#Ex. Aqui ele conta de 0 a 7 pulando de 2 em 2.
for c in range(0, 7, 2):
    print(c)
print('FIM!')
#Aqui ele retornaria(contaria): 0, 2, 4, 6/ FIM!

#Ex. Aqui ele faria a contagem do número solicitado.
numero = int(input('Digite um número: '))
for c in range(0, numero + 1):
    print(c)
print('FIM!')
#Caso você solicite '5', ele faria uma contagem de 0 a 5.

#Ex.
for c in range(0, 3):
    numero = int(input('Digite um número: '))
print('FIM!')
#Aqui ele repetirá a pergunta 3 vezes.

#Ex.
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n
print(f'O somatório de todos os valores foi: {s}')
#Ele fará a soma de todos os números coletados. Por conta da estrutura de repetição que vai pedir 3 números.

#Ex. 69 Atividade 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Vamos para a contagem dos fogos de artificio!')
for c in range(11, 0, - 1):
    sleep(1.0)
    print(c)
print('FOGOOOOOO!!!')

#Ex. 70 Atividade 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
from time import sleep
for c in range(0, 51, 2):
    sleep(0.2)
    print(c, end=' ')
print('Acabou!')

#Ex. 71 Atividade 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
from time import sleep
soma = 0
cont = 0
for p in range(0, 3):
    sleep(1.0)
    print('PROCESSANDO...')
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é: {soma}')

#Ex. 72 Atividade 49: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
from time import sleep
print('Vamos estudar a tabuada!\n')
numero = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1.5)
print(f'A tabuada do número: {numero} é:')
for tabuada in range(0, 11):
    sleep(0.5)
    calculo = tabuada * numero
    print(f'{numero} x {tabuada} = {calculo}')

#Ex. 73 Atividade 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}° número: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma de todos os números pares, é: {soma}')

#Ex. 74 Atividade 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('===' * 9)
print('    10 TERMOS DE UMA PA')
print('===' * 9)
print('\n')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for pa in range(primeiro, decimo + razao, razao):
    print(f'{pa}', end=' | ')
print('ACABOU!')

#Ex. 75 Atividade 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
print('Vamos verificar se o número digitado é um NÚMERO PRIMO \n')
numero = int(input('Digite um número: '))
for p in range(1, numero + 1):
    if numero % p == 0:
        print(f'{p}', end= ' ')
        total += 1
    else:
        print(f'{p}', end= ' ')
print('\n')
print(f'O número {numero} pode ser dividido {total} vezes.')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')

#Ex. 76 Atividade 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos: APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
print('Vamos inverter qualquer palavra ou frase! \n')
frase = str(input('Digite qualquer coisa: ')).lower().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('NÃO temos um PALÍNDROMO!')

#Ex. 77 Atividade 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for ano in range(1, 8):
    solicitacao = int(input(f'Em que ano a {ano}° pessoa nasceu? '))
    idade = atual - solicitacao
    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade! \nE também tivemos {totalmenor} pessoas menores de idade!')

#Ex. 78 Atividade 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de: {maior}Kg \nO menor peso lido foi de: {menor}Kg')

#Ex. 79 Atividade 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).upper().strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip().capitalize()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade >  20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'''A média de idade do grupo é de: {mediaidade} anos
O homem mas velho tem: {maioridadehomem} anos e se chama: {nomevelho}
Ao todo são: {totmulher20} mulheres com menos de: 20 anos''')
#---------------------------------------------------------------------
# Variáveis de controle
soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulheres_20 = 0

# Laço para 4 pessoas
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')

    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    # Verifica se é o homem mais velho
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_mais_velho = nome

    # Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        total_mulheres_20 += 1

# Calcula média
media_idade = soma_idade / 4

# Resultados
print('\n======= RESULTADOS =======')
print(f'A média de idade do grupo é de {media_idade:.1f} anos.')

if maior_idade_homem > 0:
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
else:
    print('Não houve homens cadastrados.')

print(f'Ao todo, {total_mulheres_20} mulher(es) têm menos de 20 anos.')

#Ex.
for frase in range(1, 4):
    pedido = str(input(f'Digite a {frase}° uma frase: ')).lower().strip()
    lista = pedido.count('a')
    print(f'''Na frase: {pedido}
    A letra "a" aparece {lista} vezes!''')
    print('\n')

#Ex.
from time import sleep
print('Vamos criar uma pirâmide para você! \n')
piramide = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1.0)
for numero in range(1, piramide, + 1):
    print('*' * numero)
print('ACABOU!')

#O 'for' também e conhecido como: Estrutura de repetição com variavel de controle.

#HUBLA
lista = ['Mayezer', 'Samara', 'Mayender', 1, 2, 3, 4, 5]

for itens in lista:
    print(f'Esses são os itens da lista: {itens}.')




