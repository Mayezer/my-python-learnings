#1° MUNDO
#Aula 01 a 04
#(print) significa ESCREVA.
#(print) serve para transcrever certos comandos guardados na memoria.
#Sempre acompanhado de (''), ou juntando certas palavras ou números com (,) ou (+).
# (,) e (+) tem funções um pouco diferentes dependendo se são letras, números ou input.

#Ex.01: atividade 001
print ('Olá, Mundo!')

#O símbolo de (=) significa RECEBER, não igual.

#Ex.02:
nome = 'Qual o seu nome? '
idade = 'Qual a sua idade? '
peso = 'Qual o seu peso? '

print (nome, idade, peso)

#(input) significa LEIA.
#(input) serve para definir uma função específica.

#Ex.03: atividade 002
nome = input ('Qual o seu nome? ')

print ("Olá", nome, '! Prazer em te conhecer')

#Ex.04:
dia = input ('Dia = ')
mes = input ('Mês = ')
ano = input ('Ano = ')

print ('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

#Aula 06
#(int), (float), (bool) e (str).
#(int) Números inteiros: Ex. 2, -8, 0 ou até mesmo 9586.
#(float) Números ponto flutuante(números reais): Ex. 5.5, 0.086, 7.0 ou até mesmo -15.654.
#(bool) Valor boleano, que só aceita dois valores, sempre começando com letra maiúscula: Ex. True ou False(Verdadeiro ou Falso)
#(str) São palavras, sempre entre aspas. Ex. 'Olá', '7.2' ou até mesmo aspas vazias, ''.

#Ex.05 atividade 003
#n1 = Número 01
#n2 = Número 02
n1 = int(input ('Primeiro número: '))
n2 = int(input ('Segundo número: '))

print ('A Soma é: ', n1 + n2)

#Tipo primitivo

#Ex.06
#n01 = Número 01
n01 = input('Digite um valor: ')
print (type(n01))

#Ex.07
#n02 = Número 01
n02 = int(input('Digite um valor: '))
print (type(n02))

#Ex.08
#n03 = Número 01
#n04 = Número 02
n03 = int(input ('Primeiro número: '))
n04 = int(input ('Segundo número: '))
soma = n03 + n04

print ('A Soma é: ', soma)

#Quando se junta uma string na outra, se chama: Concatenação

#Ex.09
#n05 = Número 01
#n06 = Número 02
n05 = int(input ('Primeiro número: '))
n06 = int(input ('Segundo número: '))
soma = n03 + n04

print ('A Soma entre: ', n05, ' e ', n06, 'é: ', soma)

#Chaves {} se chama mascara.
#(format) serve para dar certos valores.

#Ex.10
#n07 = Número 01
#n08 = Número 02
n07 = int(input ('Primeiro número: '))
n08 = int(input ('Segundo número: '))
soma = n07 + n08
# print ('A Soma entre: ', n07, ' e ', n08, 'é: ', soma)
print ('A soma entre {} e {} vale: {}'.format(n07, n08, soma))

#Outra forma de escrever
#n4 = Número 01
#n5= Número 02
n4 = int(input ('Primeiro número: '))
n5 = int(input ('Segundo número: '))
calculo = n4 + n5
print (f'A soma de {n4} e {n5} é {calculo}')

#Ex.11
num = float(input('Digite um valor: '))
print(num)
#7.0

num01 = str(input('Digite um valor: '))
print(num01)
#7

num02 = bool(input('Digite um valor: '))
print(num02)
#Se responder um número vira True(Verdadeiro), e se só apertar enter vira False(Falso).

num03 = (input('Digite um valor: '))
print(num03.isnumeric())
#(isnumeric) vai dizer se é possivel converter esse valor no momento em um número com o tipo primitivo int antes dele.
#3 = True Porque é número.
#3a = False Porque não é número.

num04 = (input('Digite um valor: '))
print(num04.isalpha())
#(isalpha) se é letra.
#www = True Porque só tem letras.
#123 = Falso Porque é números.

num05 = (input('Digite um valor: '))
print(num05.isalnum())
#(isalnum) è alfanúmerico Alfabeto e Númerico.
#6, 3a ou 0i = São True, por terem números e letras.
#( ) Espaço é False.

num06 = (input('Digite um valor: '))
print(num06.isupper())
#Serve para saber se só tem letras maiúculas.
#E etc.. Existem vários métodos de testes de tipos.

#Ex.12 Atividade 004
tipo1 = input('Me diz algo ai: ')

print('O tipo primitivo desse valor é: ', type(tipo1))
print('É maiúscula:', tipo1.isupper())
print('É alfabético: ', tipo1.isalpha())
print('É alfanúmerico: ', tipo1.isalnum())
print('É um número:', tipo1.isnumeric())
print('É um espaço em branco: ', tipo1.isspace())
print('É um decimal: ', tipo1.isdecimal())
print('É minúcula:', tipo1.islower())

#Aula 07
#Operações aritméticas.
#(+) Adição, (-) Subtração, (*) Multiplicação, (/) Divisão, (**) Potência(raiz quadrada), (//) Divisão Inteira e (%) Resto da Divisão.
#(==) Significa igual.

#5 + 2 == 7
#5 - 2 == 3
#5 * 2 == 10
#5 / 2 == 2.5
#5 ** 2 == 25
#5 // 2 == 2
#5 % 2 == 1

#Ordem das operações: 1° - (), 2° - **, 3° - *, /, // e %, 4° - + e -.

#Ex.13
#5 + 3 * 2 == 11
#3 * 5 + 4 ** 2 == 31
#3 * (5 + 4) ** 2 == 243
#oi * 5 == oioioioioi

#Ex.14
#{:=^20}, {:<20}, {:>20}
nome = input('Qual o seu nome?')
print(f'Prazer em conhecer você {nome:=^20}!')
#Qual o seu nome? Mayezer
#Prazer em conhecer você ======Mayezer=======!

#Ex.15
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é: {}, \n O produto é: {} \n Divisão é: {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é: {} e potência é: {}'.format(di,e))

#(\n) Serve para cortar textos, (quebrar).
#(end=' ') Serve para tudo finalizar na mesma linha. Sendo vazio ou não.

#Ex.16 Atividade 005 - Enunciado: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
n1 = n - 1
n2 = 1 + n

print('Analisando o valor: {}, seu antecessor é: {} e o sucessor é: {:/^10}'.format(n, n1, n2, end=' '))

#Ex.17 Atividade 006 - Enunciado: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
teste = int(input('Insira seu número: '))
dobro = 2 * teste
triplo = 3 * teste
raiz = teste ** 0.5

print('O dobro de {} é: {} , \n O triplo de {} é: {}, \n A raiz quadrada de {} é: {:.3f}'.format(teste, dobro, teste, triplo, teste, raiz))

#Ex.18 Atividade 007 - Enunciado: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
teste1 = float(input('Primeira nota do aluno: '))
teste2 = float(input('Segunda nota do aluno: '))
teste3 = (teste1 + teste2) / 2

print('A média entre {} e {} é igual a {}'.format(teste1, teste2, teste3))

#Ex.19 Atividade 008 - Enunciado: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a: \n {}cm \n {}mm'.format(m, cm, mm))

#Ex.20 Atividade 009 - Enunciado: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
tabuada = int(input('Me fale um número, e eu te falo a tabuada de multiplicação: '))
n0 = 0 * tabuada
n1 = 1 * tabuada
n2 = 2 * tabuada
n3 = 3 * tabuada
n4 = 4 * tabuada
n5 = 5 * tabuada
n6 = 6 * tabuada
n7 = 7 * tabuada
n8 = 8 * tabuada
n9 = 9 * tabuada
n10 = 10 * tabuada

print(f'0 x {tabuada} igual a: {n0}')
print(f'1 x {tabuada} igual a: {n1}')
print(f'2 x {tabuada} igual a: {n2}')
print(f'3 x {tabuada} igual a: {n3}')
print(f'4 x {tabuada} igual a: {n4}')
print(f'5 x {tabuada} igual a: {n5}')
print(f'6 x {tabuada} igual a: {n6}')
print(f'7 x {tabuada} igual a: {n7}')
print(f'8 x {tabuada} igual a: {n8}')
print(f'9 x {tabuada} igual a: {n9}')
print(f'10 x {tabuada} igual a: {n10}')

#Ex.21 Atividade 010 - Enunciado: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1.00 = R$ 6.25
cart = float(input('Quanto de dinheiro você tem na carteira: R$'))
dolar = cart / 6.5

print(f'Com R${cart} você pode comprar: US${dolar:.2f}')

#Ex.22 Atividade 011 - Enunciado: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
m2 = lar * alt
tinta = m2 / 2

print(f'Sua parede tem uma dimensão de {lar}x{alt} e sua área é de: {m2}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')

#Ex.23 Atividade 012 - Enunciado: Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
pre = float(input('Qual o preço do produto: R$'))
desc = pre * 0.05
val = pre - desc

print(f'O preço do produto é: R${pre}.\nO desconto de 5% é: R${desc}.\nE o valor com desconto é: R${val}')

#Ex.24 Atividade 013 - Enunciado: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual é o salário do Funcionário: R$'))
mult = sal * 0.15
aum = sal + mult

print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, irá receber: R${aum:.2f}.')

#Ex.25 Atividade 014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c1 = float(input('Informe a temperatura em °C: '))
f1 = (c1 * 1.8 + 32) #Também da para fazer: f1 = ((9 * c1) / 5 + 32)

print(f'A temperatura em °C é: {c1:.1f}°C (Celsius), que corresponde a: {f1:.1f}°F (Fahrenheit).')

#Ex.26 Atividade 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = float(input('Quantos dias alugados: '))
km = float(input('Quantos KM rodados: '))

c1 = dia * 60
c2 = km * 0.15
c3 = c1 + c2

print(f'O valor de dias alugados é: R${c1:.2f}\nO valor de KM rodados é: R${c2:.2f}\nO valor total a se pagar é: R${c3:.2f}')

#Aula 08
#Utilizando Módulos

#import: Vai importar todas as funcionalidades de um módulo. Generalista.
#from import: Vai importar somente as funcionalidades que eu escolher. Especifico.
#Dentro da biblioteca - math:
#ceil - Arredonda para cima / floor - Arredonda para baixo / trunc - Elimina da virgula pra frente sem fazer arredondamento nenhum
#pow - Potencia == ** / sqrt - Calcular raiz quadrada / factorial - Calcular fatorial

#python.org(site oficial) Você pode ir em Docs, Library reference e estudar certas funcionalidades por lá.
#Continuando no site, você pode ir em "PyPI" que é o índice de pacotes extras, que você mesmo pode criar certos modulos, ou baixar de outras pessoas.
#Como instalar, use "import" e coloque o nome do pacote, clique na lâmpada vermelha, e instale o pacote.
#Você pode usar o comando "import" e apertar "CTRL + ESPAÇO" e abrir uma lista de coisas que você pode importar por padrão.


#Ex.27
import math
n1 = int(input('DIGITE UM NÚMERO: '))
raiz = math.sqrt(n1)

print (f'A raiz de {n1} é igual a: {raiz:.2f}.')

#Ex.28
from math import sqrt
n1 = int(input('DIGITE UM NÚMERO: '))
raiz = sqrt(n1)

print (f'A raiz de {n1} é igual a: {raiz:.2f}.')

#Ex.29
from math import sqrt, floor
n1 = int(input('DIGITE UM NÚMERO: '))
raiz = sqrt(n1)

print (f'A raiz de {n1} é igual a: {floor(raiz):.2f}.')

#Ex.30
import random
n1 = random.random

print(n1)

#Ex.31
import random
n1 = random.randint(1, 10)

print(n1)

#Ex.32 modulo importado
import emoji

print(emoji.emojize('Olá, Mundo! :thumbs_up:'))

#Ex.33 modulo importado
import emoji

print(emoji.emojize('Olá, Mundo! 🌎'))

#Ex.34 Atividade 016 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n1 = float(input('Digite um número: '))
i1 = trunc(n1)

print (f'O número {n1} tem como parte inteira {i1}.')
#Ou
n1 = float(input('Digite um número: '))
print (f'O número {n1} tem como parte inteira: {int(n1)}.')
#Nem sempre precisamos importar a biblioteca.

#Ex.35 Atividade 017 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
print('Vamos calcular o comprimento da hipotenusa.')

from math import hypot
n1 = float(input('Digite a medida do cateto oposto: '))
n2 = float(input('Digite a medida do cateto adjacente: '))
n3 = hypot(n1, n2)

print(f'Calculando {n1} e {n2} o comprimento da hipotenusa é: {n3:.2f}.')
#Também podemos fazer somente com os símbolos matemáticos, seguindo a fórmula matematica: n3 = (n1 ** 2 + n2 ** 2) ** (1/2)
#Sem precisar importar a biblioteca.

#Ex.36 Atividade 018 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n1 = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))

print (f'O ângulo de {n1:.1f} tem o SENO de: {seno:.2f}\nO ângulo de {n1:.1f} tem o COSSENO de: {cos:.2f}\nO ângulo de {n1:.1f} tem a TANGENTE de: {tan:.2f}')
#Ou
from math import sin, cos, tan, radians

n1 = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(n1))
cos = cos(radians(n1))
tan = tan(radians(n1))

print (f'O ângulo de {n1:.1f} tem o SENO de: {seno:.2f}\nO ângulo de {n1:.1f} tem o COSSENO de: {cos:.2f}\nO ângulo de {n1:.1f} tem a TANGENTE de: {tan:.2f}')

#Ex.37 Atividade 019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
print ('Vamos sortear um nome!')
from random import choice
n1 = str(input('Digite o 1° nome: '))
n2 = str(input('Digite o 2° nome: '))
n3 = str(input('Digite o 3° nome: '))
n4 = str(input('Digite o 4° nome: '))
s1 = choice([n1, n2, n3, n4])

print (f'O nome sorteado é: {s1}')

#Ex.38 Atividade 020 O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = str(input('1° nome: '))
n2 = str(input('2° nome: '))
n3 = str(input('3° nome: '))
n4 = str(input('4° nome: '))
n5 = [n1, n2, n3, n4]
random.shuffle(n5)

print (f'A ordem é: {n5}')

#Ex.39 Atividade 021 Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#Aula 09
#Manipulando texto

Frase = 'Curso em Vídeo Python'
#[C][u][r][s][o] [ ] [e][m] [ ] [V][í][d][e][o] [ ] [P][y][t][h][o][n]
# 0  1  2  3  4   5   6  7   8   9  10 11 12 13  14  15 16 17 18 19 20
#Fatiamento - Letras maiusculas e minusculas tem diferença
#Sempre um número a "mais"
#frase[9:13] é igual a: Víde
#frase[9:21] é igual a: Vídeo Python
#frase[9:21:2] é igual a: VdoPto (Salta de 2 em 2 caracteres, em sequencia)
#frase[:5] é igual a: Curso (Vai começar do inicio, até 5, que seria até a letra 4)
#frase[15:] é igual a: Python (Vai da onde você solicitou o começo, e vai até o final)
#frase[9::3] è igual a: VePh (Pula de 3 em 3 caracteres)

#Análise de string

#len(frase) é igual a: (Qual o comprimento da frase, que seria 21 caracteres, micro espaços na memoria)
#frase.count('o') é igual a: (Quantos 'o' existem na frase, que seria 3)
#frase.count('o',0, 13) é igual a: (Conta fazendo o fatiamento entre o comando soliciatado, no caso, 1 'o')
#frase.find('deo') é igual a: (Quantas vezes foi encontrado 'deo', diz em qual posição começa que seria posição [11])
#frase.find('Android') é igual a: (Não existe, ele vai me retornar o valor de -1, pois não foi encontrado)
#'Curso' in frase é igual a: (Vai me dizer que existe a frase, e vai dar o resultado - True, pois existe)

#Transformação

#frase.replace('Python', 'Android') é igual a: (Muda a frase 'Pyhton' por 'Android', trocando de uma forma secundaria)
#frase.upper() é igual a: (Transforma tudo em maiusculo)
#frase.lower() é igual a: (Transforma tudo em minusculo)
#frase.capitalize() é igual a: (Joga os caracteres em minusculo, mas a primeira letra de cada frase, é mudada para maiusculo)
#frase.title() é igual a: (Analisa cara palavra, e quebra cada uma delas, deixando todas com a primeira letra maiuscula)
#frase.strip() é igual a: (Remove os espaços do começo e do fim da frase, não remove os espaços entre cada frase)
#frase.rstrip() é igual a: (Com a variação 'r' (direita) remove somente os espaços do final da frase)
#frase.lstrip() é igual a: (Coma a variação 'l' (esquerda) remove somente os espaço do começo da frase)

#Divisão

#frase.split() é igual a: (Divide os espaços entre cada frase, gerando uma lista)

#Junção

#'-'.join(frase) é igual a: (Ele junta todo elemento de frase, e usa o separado '-' nos espaços)

#Todo método tem '.()' no final.

#Ex.40 Atividade 22 Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
while True:
    nome = str(input('Digite seu nome completo: ')).strip()
    print('\n')

    print('Analisando seu nome...')
    print('\n')

    print(f'Seu nome em letras MAIÚSCULAS é: {nome.upper()}.')
    print(f'Seu nome em letras minúsculas é: {nome.lower()}.')
    print(f'Seu nome tem {len(nome) - nome.count(' ')} letras ao todo.')
    print(f'Seu nome em uma lista é: {nome.split()}')
    separa = nome.split()
    print(f'Seu prmeiro nome é: {separa[0]} e ele tem: {len(separa[0]) - separa.count(' ')} letras.')
    separa2 = nome.split()
    print(f'Seu sobrenome é: {separa2[1:]} e ele é dividido em: {len(separa2[1:]) - separa2.count(' ')} partes.')
    print('\n')

    novo = input('Deseja fazer outro teste? (sim/não): ')
    if novo == 'não':
        print('Obrigado por fazer parte desse teste! :)')
        break
    else:
        print('Fique a vontade, teste mais nomes! :D')
        print('\n')

#Ex.41 Atividade 23 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n1 = int(input('Informa um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('\n')
print (f'Analisando o número: {n1}...')
print('\n')
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

#Ex.42 Atividade 24 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper()=='SANTO')

#Ex.43 Atividade 25 Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome tem SILVA: {'silva' in nome.lower()}')

#Ex.44 Atividade 26 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra |A|, aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra |A| apareceu na posição {frase.find('A') + 1}.')
print(f'A última letra |A| apareceu na posição {frase.rfind('A') + 1}.')

#Ex.45 Atividade 27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
nome0 = nome.split()
print('\n')
print(f'Muito prazer em te conhecer {nome}.')
print('\n')
print(f'Seu primeiro nome é: {nome0[0]}.')
print(f'Seu último nome é: {nome0[len(nome0) - 1]}.')

#Aula 10
#Condições simples e compostas

#if (Se for)
#else (Se NÃO for)

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

#Aula 11 - AULA BÔNUS
#Cores no terminal
#Pesquise sobre: colorsys - é uma biblioteca de cores.
#Todo código ANSI para cor começa com: \033[m
#Representação de cor em python: \033[m - Padrão do terminal, volta pro ambiente normal.
#1° style - Código do comportamento |;| 2° text - Código do texto |;| 3° back - Background - Código cor de fundo
#1° Estilo da fonte(negrito, normal ou até sublinhada) | 2° Cor do texto | 3° Cor do fundo
#style - 0 - None(nada) | 1 - Bold(negríto) | 4 - Underline(sublinhado) | 7 - Negative(inverte as cores de fundo e das letras)
#text - 30(preto) | 31(vermelho) | 32(verde) | 33(amarelo) | 34(azul) | 35(rosa - magenta) | 36(ciano) | 37(cinza ou branco)
#back - 40(preto) | 41(vermelho) | 42(verde) | 43(amarelo) | 44(azul) | 45(rosa - magenta) | 46(ciano) | 47(cinza ou branco)
#Ex. \033[0;33;44m

#Ex: 56 Testes de cores
#\033[0;30;41m - Estilo normal, texto branco e fundo vermelho.
#\033[7;30m - Letra preta e fundo branco.
#Mostrando em código__________________________________________
#print('\033[1;31;40mOlá, Mundo!') - Frase em negríto, na cor vermelha e fundo preto.
#print('\033[0;31;42mOlá, Mundo!\033[m') - Limita o fundo, somente até o fim da frase.
#print('O valor de \033[31m{}\033[m é de \033[m{}\03[m!!!') - Colocando cores somente em letras, números ou frases isoladas.
#Ex: 57_______________________________________________________
nome = str(input('Qual o seu nome? '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print(f'Olá meu amigo {cores['azul']}{nome}{cores['limpa']}, seja bem vindo!!!')
#Código mais limpo visualmente e fácil crompreensão das cores.

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

#Ex.
c = 1 #Contador começa com 1.
while c < 10: #Enquanto o contador for menor do que 10 ou não chegar a 10.
    print(c)
    c = c + 1 #Porque quando ele volta, quero somar +1 no c.
print('FIM!')

#Ex. Condição de parada
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

#Ex. Conseguindo criar laços(loop) indeterminados, sem um limite
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? (S/N): ')).upper().strip()
print('FIM!')

#Ex. A gambiarra rsrsrsrs
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')

#Ex. 80 Atividade 57:
#Existe varias formas de ser escrito o mesmo código.
while True:
    sexo = str(input('Informa se sexo: [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        print(f'Sexo {sexo} registrado com sucesso!')
        break
    else:
        print('Dados invalidos. Informe corretamente!')
print('\n')
print('Fim!')
#-----------------------------------------------------------------------
while True:
    sexo = str(input('Informa se sexo: [M/F]: ')).upper().strip()
    if sexo in ['M', 'F']:
        print(f'Sexo {sexo} registrado com sucesso!')
        break
    else:
        print('Dados invalidos. Informe corretamente!')
print('\n')
print('Fim!')
#-----------------------------------------------------------------------
sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0] #Esse [0] Serve para pegar somente a primeira letra da frase ou palavra digitada.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informa seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

#Ex. 81 Atividade 58:
print('''Sou uma máquina pensante...
E acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? (O.o)\n''')
from random import randint
tentativas = 0
aleatorio = randint(1,10)
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

#Ex. Atividade 59:
numero0 = int(input('Primeiro valor: '))
numero1 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Números novos
    [ 5 ] Finalizar o programa''')
    pedido0 = int(input('>>>> Qual é a sua opção? '))
    print('==' * 17)
    if pedido0 == 1:
        soma0 = numero0 + numero1
        print(f'A SOMA entre {numero0} e {numero1} é: {soma0}\n')
    elif pedido0 == 2:
        multiplicacao0 = numero0 * numero1
        print(f'A MULTIPLICAÇÃO entre {numero0} e {numero1} é: {multiplicacao0}\n')
    elif pedido0 == 3:
        if numero0 > numero1:
            print(f'O número maior é: {numero0}\n')
        elif numero0 < numero1:
            print(f'O número maior é: {numero1}\n')
        elif numero0 == numero1 or numero1 == numero0:
            print('Os números são iguais!\n')
    elif pedido0 == 4:
        numero2 = int(input('Digite o primeiro novo valor: '))
        numero3 = int(input('Digite o segundo novo valor: '))
    elif pedido0 == 5:
        print('Fim do programa! Obrigado por utilizar nossos serviços.')
        break
    else:
        print('Opção INVÁLIDA, tente novamente!')

#Ex. Atividade 60
from time import sleep
fatorial = 1
calculo = int(input('''Digite um número para 
calcular o seu Fatorial: '''))
i = calculo
while i > 0:
    fatorial *= i
    i -= 1
print('PROCESSANDO...')
sleep(1.0)
print('\n')
print(f'Calculando: {calculo}! = {fatorial}', end='')

#Ex. Atividade 61
print('GERADOR DE PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    cont += 1
print('FIM!!')

#Ex. Atividade 62
print('GERADOR DE PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('\n')
print(f'Progressão finalizada com: {total} termos mostrados!')

#Ex. Atividade 63
print('sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t0 = 0
t1 = 1
print(f'{t0} - {t1}', end='')
cont = 3
while cont <= n:
    t2 = t0 + t1
    print(f' - {t2}', end='')
    t0 = t1
    t1 = t2
    cont += 1
print(' - FIM!!')

#Ex. Atividade 64
num = cont = soma = 0
nume = int(input('Digite um número: '))
print('Caso queira parar digite o número: 999')
print('\n')
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
    print('Caso queira parar digite o número: 999')
    print('\n')
print(f'Você digitu {cont} números e a soma entre eles foi de: {soma}.')

#Ex. Atividade 65
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi: {media}')
print(f'O maior valor foi: {maior} e o menor foi: {menor}')

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

#Mundo 3 -------------------------------------------------------------------------------------------------

#Aula 16
#Variáveis Compostas - (Tuplas)

#Variavel simples
#Ex.
#lanche = 'hamburguer'
#Só cabe uma variável no espaço com o mesmo nome
#lanche = 'suco'

#Tuplas - Podem receber mais de um 'espaço'(variável)
#Sendo assim variáveis compostas podem armazenar vários valores, com números ilimitados, somente tendo que definir cada uma delas
#Existem 3 formas de serem feitas, sendo elas: Tuplas, listas ou dicionarios.
#E podemos manipular uma tupla
#E podemos acessar os elementos da tupla usando indices começando sempre por 0.
#Supondo que temos 4 variáveis, cada variável recebe um número(indice), representados por: 0, 1, 2, 3

#Ex.
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche) #Ele puxa a tupla inteira, porém retorna com () e ''
print(lanche[2]) #Nesse caso ele retornaria: Pizza
print(lanche[0:2]) #Aqui ele retorna de 0 a 2, no caso: Hamburguer e Suco. Lembrando que sempre o ultimo número é cortado.
print(lanche[1:]) #Ele retorna so número 1 em diante, sendo assim: Suco, Pizza e Pudim
print(lanche[:2]) # Ele retorna: Hmaburguer e Suco. E lembrando, a Pizza não foi puxado porque o python sempre desconsidera o último elemento.
print(lanche[-1]) #Ele retorna o: Pudim. Puxando da direita pra esquerda(Do final ao começo). Se colocar -2, ele puxa: Pizza, -3 Puxa: Suco
#Sendo assim, o Hamburguer tem o indice 0 e -4
print(lanche[-2:])
print(lanche[:-2])
#Também podemos fazer o fatiamento com os indices negativos, lembrando le puxa da direita para a esquerda.

#Ex.
#O método ou função 'len', tendo referencia a 'lens' que significa comprimento
len(lanche) #Ele retorna quantos elementos tem na variável lanche, tendo a resposta: 4

#Ex.
#Podemos usar as estruturas de repetição
for c in lanche:
    print(c) #Ele retornará: Hamburguer, mas quando ele volta por ser um loop ele retorna: Suco e assim em diante... Até finalizar a lista.
    #Retorna cada nome bonitinho, sem () e ''
#Conceito importante: Supondo que você queira trocar Pudim por sorvete, não tem como. As tuplas são IMUTÁVEIS(Não podem ser trocadas)

#Ex.
for comida in lanche: #lanche entrou no lugar do range, por já ter uma tupla, um indice
    print(f'Eu vou comer: {comida}')
print('\nEu comi muitoooo!')

#Ex.
for cont in range(0, len(lanche)):
    print(cont) #Ele retorna: 0, 1, 2, 3 Por conta do len
    print(lanche[cont]) #Ele retorna: Hamburguer, Suco, Pizza e Pudim
    print(f'Eu vou comer: {lanche[cont]}') #Exibe da mesma maneira, mas com a mensagem do print
    print(f'Eu vou comer: {lanche[cont]} na posição {cont}')  #Exibe da mesma maneira, porém com a contagem de cada posição dos indices

#Ex.
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}') #Ele a mensagem e as comidas, porém mostrando seus indices

#Podemos usar o comando: sorted. Que significa organizado. Então ele vai me retornar em ordem alfabética
#Ele não autera nada, ele coloca em ordém
#Porém são tirados os () e são colados os [], transformando em listas, porque lembrando, tuplas são imutaveis
#Ex.
print(sorted(lanche)) #Essa é a forma de usar

#Ex.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #Ele junta as tuplas, dando o resultado: (2, 5, 4, 5, 8, 1, 2)
#Caso seja
d = b + a
print(d) #Ele junta e retorna a tupla que vem primeiro: (5, 8, 1, 2, 2, 5, 4)
print(len(d)) #Ele retorna 7, pois existem 7 indices juntando as tuplas
print(d.count(5)) #Ele retorna: 2, pois ele conta quantas vezes o número 5 aparece
print(d.index(8)) #Ele me mostra em qual posição está o número solicitado, no caso o 8, estando na posição: 1 Lebrando que a contagem começa em 0
#O idex só retorna a primeira posição
print(d.index(5, 1)) #Ele retorna: 5, porque o outro 5 está na posição 0, então ele só retorna um número 5.
#Chamamos isso de deslocamento

#Ex.
pessoa = ('Mayezer', 25, 'M', 120.50)
print(pessoa) #Ele retorna tudo, não importa se é letras ou números

#O comando del serve para deletar da memória
#del(pessoa)

#Ex. Atividade 73: Crie uma tupla preenchida com os 12 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time Bota Fogo.
times = ('Flamengo', 'Fluminense', 'Palmeiras', 'Paisandu', 'Bota Fogo', 'Santos',
         'Real Madrid', 'Cotinthians', 'Atlético', 'Grêmio', 'Cruzeiro', 'Coritiba')

print(f'Lista de times do Brasileirão: {times} \n')
print(f'Os 05 primeiros são: {times[0:5]} \n')
print(f'Os 04 últimos são: {times[-5: -1]} \n')
print(f'Os times em ordem alfabética: {sorted(times)} \n')
print(f'O {times.index("Bota Fogo")} está na 5º posição')

#Ex. Atividade 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = tuple(randint(1, 10) for _ in range(5))

print('Os valores são:', *numeros) #O * serve para tirar as () em volta dos números sorteados
print('O maior valor sorteado é:', max(numeros))
print('O menor valor sorteado é:', min(numeros))

#Ex. Atiidade 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#Usando while
contagem = 0
numeros = ()  # Cria uma tupla

while True:
    numero = int(input('Digite um número: '))
    numeros += (numero,)  # Concatena criando nova tupla
    contagem += 1
    if contagem == 4:
        break

print('\nVocê digitou os números:', *numeros)
if 9 in numeros:
    print(f'O número 9 apareceu: {numeros.count(9)} vezes')
else:
    print('O número 9 não apareceu em nenhum momento.')

if 3 in numeros:
    print(f'O número 3 apareceu primeiro na: {numeros.index(3) + 1}ª posição')
else:
    print('O número 3 não apareceu em nenhum momento.')

par = tuple(n for n in numeros if n % 2 == 0)
print(f'Os números pares digitados foram: {par}')
#--------------------------------------------------------------------------------------------------------

#Usando for
numeros = () #Cria uma tupla
for c in range(4):
    numero = int(input('Digite um número: '))
    numeros += (numero,) #Concatena criando nova tupla

print('\nVocê digitou os números:', *numeros)
if 9 in numeros:
    print(f'O número 9 apareceu: {numeros.count(9)} vezes') #Conta quantos números 9 aparecem
else:
    print('O número 9 não apareceu em nenhum momento.')

if 3 in numeros:
    print(f'O número 3 apareceu primeiro na: {numeros.index(3) + 1}º posição') #Puxa a primeira posição que o número 3 aparece.
else:
    print('O número 3 não apareceu em nenhum momento.')

par = tuple(n for n in numeros if n % 2 == 0)
print('Os números pares digitados foram:', par)

#Ex. Atividade 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('LÁPIS', 1.75, #TUPLA
            'BORRACHA', 2.00,
            'CADERNO', 15.90,
            'ESTOJO', 25.00,
            'TRANSFERIDOR', 4.20,
            'COMPASSO', 9.99,
            'MOCHILA', 120.32,
            'CANETAS', 22.30,
            'LIVRO', 34.90)

print('=' * 40)
texto = 'LISTAGEM DE PREÇOS'
print(f'{texto:^40}')
print('=' * 40)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
    else:
        print(f'R${listagem[posicao]:>8.2f}')

print('==' * 20)

#Ex. Atividade 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aàáâãeèéêíìiîoòóôõ':
            print(letra, end=' ')


#Aula 17
#Listas

#As listas usam: []
#Listas podem ser modificadas

#Ex.
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picolé' #Listas são mutaveis(podem sofrer mudanças), então sairia 'Pudim' e entraria 'Picolé'
lanche.append('Cookie') #Cria uma nova variável(valor), sendo assim existindo um novo valor: [4]
lanche.insert(0, 'Cachorro Quente') #Adiciona uma nova variável(valor) na posição solicitada, sendo assim 'Cachorro Quente' na posição [0]
#Que ficaria, [0]Cachorro Quente, [1]Hamburguer, [2]Suco, [3]Pizza, [4]Picolé, [5]Cookie
#Vamos ver formas de apagar variáveis da lista --------------------------------------------
del lanche[3] #Apaga a variável(valor) solicitada, no caso: [3]Pizza
lanche.pop(3) #Geralmente usado para apagar o último elemento, mas também pode ser usado para a variável(valor) solicitado.
lanche.pop() #Geralmente usado para apagar o último elemento, mas também pode ser usado para a variável(valor) solicitado.
lanche.remove('Pizza') #Remove a variável(valor) mas pelo o nome.
#Lembrando que quando a variável(valor) é eliminada, os indices também mudam.
#Ficando então: [0]Cachorro Quente, [1]Hamburguer, [2]Suco, [3]Picolé
#Não pode remover algo que já não existe na lista, se não da erro
if 'piza' in lanche: #Verifica se existe a variável(valor) 'Pizza' na lista, se existe, ele remove, se não, não faz nada.
    lanche.remove('Pizza')

#Podemos criar listas através de: .range()
valores = list(range(4, 11)) #Faz uma contagem de 4 até 10, criando uma estrutura de 7 variáveis(valores)

valoress = [8, 2, 5, 4, 9, 3, 0]
valoress.sort() #Ordena todas as variáveis(valores) em ordem crescente - [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse = True) #Ordena todas as variáveis(valores) em ordem decrescente - [9, 8, 5, 4, 3, 2, 0]
len(valoress) #Retorna a quantos elementos tem na lista, no caso, 7, pois a contagem começa no número 0

#Ex.
num = [2, 5,9 ,1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
num.pop()
num.remove(2) #Só remove o primeiro número [2]

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5!')

print(num)
print(f'Essa lista tem {len(num)} elementos!')

#Ex.
valor = list() #Essa é outra maneira de 'escrever' uma lista. Mas poderiamos usar: valor = [] | Funcionaria igual.
valor.append(5)
valor.append(9)
valor.append(4)

for v in valor:
    print(f'{v}...')

for c, g in enumerate(valor):
    print(f'Na posiçãooooooooo {c}, encontrei o valor: {g}!')
print('Cheguei ao final da lista.')

#Ex.
valorees = []
for cont in range(0, 5):
    valorees.append(int(input('Digite um valor: ')))

for c, g in enumerate(valorees):
    print(f'Na posiçãooooooooo {c}, encontrei o valor: {g}!')
print('Cheguei ao final da lista.')

#Ex.
a = [2, 3, 4, 7]
b = a
b[2] = 8 #Mexe nas duas lista, pois elas ficam igualadas, cria uma ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#----------------------------------------------------------------------------
a = [2, 3, 4, 7]
b = a[:] #Faz 'b' receber todos os itens de 'a', faz uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Ex. Atividade 78
valores = []
for posicao in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {posicao}: ')))

print('=' * 35)
print('Você digitou os valores:', *valores)
print('\n')

print(f'O maior valor digitado foi {max(valores)} nas posições: {valores.index(max(valores))}... ')
print(f'O menor valor digitado foi {min(valores)} nas posições: {valores.index(min(valores))}...')

#Ex. Atividade 79
lista = []

while True:
    lista.append(int(input('Digite um Valor: ')))
    print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar: [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('\n')
        print('==' * 35)
        print('Vamos aos resultados...')
        break
    else:
        print('Opção INVÁLIDA! Tente novamente.')

lista.sort()
print('Você digitou os valores em lista:', *lista)

#Ex. Atividade 80
import bisect #O módulo bisect oferece funções para inserir elementos em uma lista já ordenada e manter essa ordenação sem precisar usar sort() constantemente

lista = list()
print('Sua lista está vazia. \n')

for _ in range(0, 5): #O underscore (_) em loops é uma convenção bastante usada em Python para indicar que a variável de iteração não será utilizada no corpo do loop.
    #Ou seja, é apenas um “placeholder”, e reforça a ideia de que não precisamos do valor iterado—apenas queremos repetir a ação um certo número de vezes
    valor = (int(input('Digite um valor: ')))
    posicao = bisect.bisect_left(lista, valor) #Encontra a posição correta para inserir valor, de maneira que a lista permaneça ordenada.
    #Caso valor já exista na lista, a inserção ocorrerá antes de qualquer elemento igual existente — ou seja, à esquerda
    lista.insert(posicao, valor) #O método list.insert(index, elemento) insere o elemento na lista na posição especificada por index.
    #Todos os elementos a partir dessa posição são deslocados para a direita, preservando os dados.
    #Ou seja, se você quiser colocar algo no meio da lista, insert() é a ferramenta certa.
    print(f'Adicionado na posição: {posicao} da lista...')

print('=' * 36)
print('Os valores digitados em ordem foram:', *lista)
#_ em loop  Indicador de que a variável de iteração não será usada
#bisect_left    Retorna a posição correta para inserir um valor, mantendo a lista ordenada
#.insert()  Insere o valor exatamente na posição dada, deslocando os demais
#-----------------------------------------------------------------------------------------------
import bisect

lista = list()
print('Sua lista está vazia. \n')

for _ in range(0, 5):
    valor = (int(input('Digite um valor: ')))
    posicao = bisect.bisect_left(lista, valor)
    lista.insert(posicao, valor)
    print(f'Adicionado na posição: {posicao} da lista...')

print('=' * 36)
print('Os valores digitados em ordem foram:', *lista)

#Ex. Atividade 81
lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    parar = str(input('Deseje continuar? [S/N]: ')).upper().strip()[0]
    if parar == 'S':
        continue
    elif parar == 'N':
        print('Vamos aos resultados! \n')
        break
    else:
        print('Opção INVÁLIDA. Tente novamente!')

print('Você digitou a lista:', *lista)
print(f'Você digitou {len(lista)} elementos(valores).')
lista.sort(reverse = True)
print(f'O valores em ordem decrescente é:', *lista)
if 5 in lista:
    print(f'O número 5 está na posição {lista.count(5) - 1}!')
else:
    print('O número 5 não foi encontrado na lista!')

#Ex. Atividade 82
lista = list()
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('\n')
        print('Fim da simulação. Vamos aos resultados!')
        break
    else:
        print('Opção INVÁLIDA! Tente novamente.')

print('A lista completa é:', *lista)
for p, v in enumerate(lista):
   if v % 2 == 0:
       pares.append(v)
   elif v % 2 == 1:
       impares.append(v)

impares.sort()
pares.sort()
print(f'Esses são os números ímpares: {impares}')
print(f'Esses são os números pares: {pares}')

#Ex. Atividade 83
contagem = list()
expre = str(input('Digite a expressão: '))

for simb in expre:
    if simb == '(':
        contagem.append('(')
    elif simb == ')':
        if len(contagem) > 0:
            contagem.pop()
        else:
            contagem.append(')')
            break

if len(contagem) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está errada!')

#Aula 18
#Listas - Parte 2

#lista criada ['Pedro', 25]
#      índice[0], índice[1]
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0]) #== Pedro
print(dados[1]) #== 25

#Vamos ver listas dentro de listas

pessoas = list()
pessoas.append(dados[:]) #Gerando fatiamento completo da estrutura de dados usando: [:]
#Cria uma lista com a lista 'dados' dentro, fazendo com que ['Pedro', 25] se torne um único índice, o índice [0].
pessoas = [['Pedro', 25], ['Maria', 19], ['joão', 32]]
#           índice [0]  ,  índice[1]   ,  índice[2]
print(pessoas[0][0]) #== Pedro, printando o índice[0] da lista pessoas e o índice [0] da lista dados
print(pessoas[1][1]) #== 19, printando o índice[1] da lista pessoas e o índice [1] da lista dados
print(pessoas[2][0]) #== João, printando o índice[2] da lista pessoas e o índice [0] da lista dados
print(pessoas[1]) #== ['Maria', 19] printando o índice[1] da lista pessoas

#Ex.
teste = list()
teste.append('Mayezer')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'Samara'
teste[1] = 27
galera.append(teste[:])
print(galera)

#Ex.
galera = [['Mayezer', 25], ['Samara', 27], ['Mayender', 32], ['Iran', 56]]
print(galera)
print(galera[0][0])
print(galera[2][1])
print(galera[3])
for pessoa in galera:
    print(pessoa) #Retorna toda a lista
    print(pessoa[0]) #Retorna todos os índices [0] da lista
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.') #Retorna todos os nomes e suas idades

#Ex.
galera = list()
dado = list()
totaldemaior = totaldemenor = 0
for pessoas in range(0, 3):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #Limpa a lista dado e só printa a lista galera

print('\n')
print(f'Essa é a lista criada: {galera}')
print('\n')

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade!')
        totaldemaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        totaldemenor += 1

print(f'Temos {totaldemaior} maiores e {totaldemenor} menores de idade!')

#Ex. Atividade 84 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
geral = list()
dados = list()
pessoas = maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: ')))
    geral.append(dados[:])
    dados.clear()
    pessoas += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('\n')
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Vamos aos resultados!')
        break
    else:
        print('Opção INVÁLIDA! Tente novamente.')

print(f'Essa foi a lista gerada: {geral}')
print('\n')

for pessoa in geral:
    if pessoa[1] >= 80:
        print(f'{pessoa[0]} Maior(es) peso(s). Peso: {pessoa[1]}kg')
        maiorpeso += 1
    else:
        print(f'{pessoa[0]} Menor(es) peso(s). Peso: {pessoa[1]}kg')
        menorpeso += 1

print('\n')

print(f'Existem {pessoas} pessoas cadastradas.')
for quantidade in geral:
    print(f'Pessoas cadastradas: {quantidade[0]}')

#Ex. Atividade 85 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]
valor = 0 #Transforma os números guardados na lista em números inteiros em vez de string.
#Podendo assim fazer a divisão para ímpar ou par.
for numero in range(1, 8):
    valor = int(input(f'Digite o {numero}° número: '))
    if valor % 2 == 0:
       numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print('\n')

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores ímpares são: {numeros[1]}')

#Ex. Atividade 86 Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print() #Qubra a linha

#Ex. Atividade 87 Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):  # Colunas
    for c in range(0, 3):  # linhas
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):  # Colunas
    for c in range(0, 3):  # Linhas
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:  # Separa o número par
            spar += matriz[l][c]
    print()  # Qubra a linha
print('-=' * 30)

for l in range(0, 3):  # Faz a soma dos valores da 3° coluna
    scol += matriz[l][2]

for c in range(0, 3):  # Separa o maior número da segunda linha
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'A soma dos valores pares é: {spar}')
print(f'A soma dos valores da 3° coluna é: {scol}')
print(f'O maior número da segunda linha é: {mai}')

#Ex. Atividade 88 Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
from time import sleep
lista = list()

cor = {'azul':'\33[34m',
       'vermelho':'\33[31m',
       'limpa':'\33[m'}

print(f'{cor['azul']}')
print('=' * 40)
print('    SORTEADOR DE NÚMEROS - MEGA SENA  ')
print('=' * 40)
print(f'{cor['limpa']}')

while True:
    sorteador = int(input('Quantos jogos você quer sortear? '))
    print(f'{cor['vermelho']}-= -= -= SORTEANDO {sorteador} JOGOS =- =- =-{cor['limpa']}')

    for valores in range(sorteador):
        numeros = sample(range(1, 61),6)  # Isso gera uma lista de 6 números únicos entre 1 e 60, e separa para usar 6 números.
        lista.append(numeros)
        numeros.sort()
        print(f'Jogo {c + 1}: {numeros}')
        sleep(1.0)
    break

print(f'{cor['vermelho']}-= -= -= < BOA SORTE! > =- =- =-{cor['limpa']}')

#Ex. Atividade 89 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
cadastro = list()

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])

    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Aqui está os resultados!')
        break
    else:
        print('Opção INVÁLIDA! Tente novamente.')

print('==' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')

print('\n')

print('Para encerrar digite: 999')
while True:
    opcao = int(input('Mostrar notas de qual aluno: '))
    if opcao == 999:
        print('FINALIZANDO...')
        sleep(1.0)
        break
    if opcao <= len(cadastro) - 1:
        print(f'Notas de {cadastro[opcao][0]} são {cadastro[opcao][1]}')

print('<<< VOLTE SEMPRE >>>')

# Aula 19
# Dicionários - Variáveis compostas

# Estrutura de dados - Conseguindo ter índices literais
# Podendo perssonalizar os índices usando letras...

# tuplas - ()
# listas - []
# Dicionarios - {} Usamos chaves

dados = dict()  # Transforma em dicionarios
#                          Ou
dadoos = {'nome': 'Pedro',
          'idade': 25}  # Assim conseguimos personalizar os índices, sendo assim, no índice nome: temos 'Pedro' nessa 'lista'(dicionario)
#         índice:          índice:
print(dadoos['nome'])  # == 'Pedro, Porque o novo índice não é mais 0 e sim 'nome'
print(dadoos['idade'])  # == 25
dados['sexo'] = 'M'  # Foi criado um índice novo chamado 'sexo' e adicionado o 'M' de Masculino
# Sendo assim criando: dadoos{'Pedro', 25, 'M'}
#            índices:         nome  idade  sexo
del dados['idade']  # Elimina o índice inteiro da estrutura

# Ex.
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
# Existe diferença entre: item, valor e chaves
# Chamando os elementos de chaves(keys)
# Estrutura criada: filme = {'Star Wars', 1977, 'George Lucas'}
print(filme.values())  # Serve para retornar todos os valores: 'Star Wars', 1977, 'George Lucas'
print(filme.keys())  # Serve para retornar todas as chaves: 'titulo', 'ano', 'diretor'
print(filme.items())  # Serve para retornar tudo, os valores e as chaves.

# Ex.
for k, v in filme.items():
    print(f'O {k} é {v}')  # Retorna 'O titulo é Star Wars', 'O ano é 1977' e 'O diretor é George Lucas'
# k == chaves | v == valores

# Ex.
# Podemos juntar listas, tuplas e dicionarios
locadora = list()
locadora.append(filme)
# Criando assim uma lista com um dicionario dentro, podendo adiconar mais filmes, anos e diretores.
print(locadora[0]['ano'])  # Printa o ano do índice '0', sendo assim: 1977
print(locadora[2]['titulo'])  # Printa o titulo do índice '2', sendo assim 'Matrix'

# Ex.
pessoas = {'nome': 'Mayezer', 'sexo': 'M', 'idade': 25}
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():  # Para usar o items precisa de 2 laços no for
    print(f'{k} = {v}')
pessoas['nome'] = 'Jorge'  # Muda o valor 'Mayezer' para 'Jorge'
pessoas['peso'] = 120  # Adiciona um novo íncice e o valor dele

# Ex. Criando dicionário dentro de uma lista
brasil = list()
estado1 = {'uf': 'Pará', 'sigla': 'PA'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado3 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil[0])
print(brasil[0]['uf'])  # Printa Pará

# Ex.
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip()
    brasil.append(estado.copy())  # Copia sem fatiamento

for estados in brasil:
    for keys, valores in estados.items():
        print(f'O campo {keys} tem valor {valores}')
#                  OU
for estados in brasil:
    for valores in estados.values():
        print(valores, end=' ')
    print()

#Ex. Atividade 90 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dicionario = dict()

dicionario ['nome'] = str(input('Nome: ')).strip()
dicionario ['média'] = float(input(f'Média de {dicionario['nome']}: '))
print('==' * 30)

if dicionario['média'] >= 7.0:
    print(f'''    - {'nome'} é igual a {dicionario['nome']}
    - {'média'} é igual a {dicionario['média']}
    - {'situação'} é igual a Aprovado''')
elif dicionario['média'] >= 5.0:
    print(f'''    - {'nome'} é igual a {dicionario['nome']}
    - {'média'} é igual a {dicionario['média']}
    - {'situação'} é igual a Recuperação''')
else:
    print(f'''    - {'nome'} é igual a {dicionario['nome']}
    - {'média'} é igual a {dicionario['média']}
    - {'situação'} é igual a Reprovado''')

#Ex. Atividade 91 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter #Ele serve para pegar (extrair) um ou mais itens de uma sequência (como listas ou tuplas) de forma rápida e mais legível.
from random import randint
from time import sleep

jogadores = dict()

print('Valores sorteados:')
for jogo in range(1, 5):
    nome = f'jogador{jogo}' #Numera os jogadores
    jogadores[nome] = randint(1, 6) #Faz o sorteio e salva no dicionário
    sleep(0.8)
    print(f'{nome} tirou {jogadores[nome]} no dado.')

print('-*' * 13)
sleep(0.8)
print('\n== RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for indice, valores in enumerate(ranking):
    print(f'{indice + 1}° lugar: {valores[0]} com {valores[1]}.')
    sleep(0.8)

print('\nFIM!')

#Ex. Atividade 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
dados = dict()
dados['aposentadoria'] = 51

dados['nome'] = str(input('Qual seu nome: ')).strip()
dados['idade'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))

if dados['ctps'] != 0:
    idade = 2025 - dados['idade']
    print('-=' * 40)
    print(f'''- {['nome']} tem o valor: {dados['nome']}
- {['idade']} tem o valor: {idade}
- {['ctps']} tem o valor: {dados['ctps']}''')
    exit() #Encerra o programa ali mesmo.

dados['contratação'] = int(input('Ano de contratação: '))
dados['salário'] = float(input('Salário: '))

print('-=' * 40)
idade = 2025 -  dados['idade']
print(f'''- {['nome']} tem o valor: {dados['nome']}
- {['idade']} tem o valor: {idade}
- {['ctps']} tem o valor: {dados['ctps']}
- {['contratação']} tem o valor: {dados['contratação']}
- {['salário']} tem o valor: {dados['salário']:.2f}
- {['aposentadoria']} tem o valor: {dados['aposentadoria']}''')

#Ex. Atividade 93 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
gols = list()

dados['nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {dados['nome']} jogou: '))

for golsnapartida in range(partidas):
    dados['gols'] = int(input(f'Quantos gols na partida {golsnapartida + 1}: '))
    gols.append(dados['gols'])
    dados['gols'] = gols
    dados['total'] = sum(gols)

print('-=' * 40)
print(f'{dados}')
print('-=' * 40)

for k, i in dados.items():
    print(f'O campo {k} tem o valor {i}')
print('-=' * 40)

print(f'O jogador {dados['nome']} jogou: {partidas} partidas.')
for g, s in enumerate(dados['gols']):
    print(f'=> Na partida {g + 1}, fez {s} gols.')
print(f'Foi um total de {dados['total']}')

#Ex. Atividade 94 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
lista = list()
soma = media = 0

while True:
    dicionario = dict()

    dicionario['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dicionario['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if dicionario['sexo'] in ['M', 'F']: #Cria uma 'lista' e verifica se a resposta de continuar confere com a 'lista' criada.
            break
        else:
            print('ERRO! Responda apenas M ou F.')

    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

        if continuar in ['S', 'N']:
            break
        else:
            print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break

print('=-' * 40)
media = soma / len(lista)
print(f'''A) Ao todo temos {len(lista)} pessoas cadastradas.
B) A média de idade é de {media:5.2f} anos.
C) A mulheres cadastradas foram: ''', end='')
for p in lista:
    if p['sexo'] in ['F', 'f']:
        print(f'{p["nome"]} - ', end='')
print() #Serve para quebrar a linha
print(f'D) Lista das pessoas que estão acima da média: ''')
for p in lista:
    if p['idade'] >= media:
        print('=> ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n<< ENCERRADO! >>')

#Ex. Atividade 95 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista = list()

while True:
    dados = dict()

    dados['nome'] = str(input('Nome do jogador: ')).strip()
    dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou: "))

    gols = [] #Lista para armazenar gols de cada partida
    for gols_na_partida in range(dados['partidas']):
        gols.append(int(input(f"---> Quantos gols na partida {gols_na_partida + 1}: ")))
    dados['gols'] = gols[:] #Copia a lista
    dados['total'] = sum(gols) #Soma os gols dos jogadores
    lista.append(dados.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

        if continuar in ['S', 'N']:
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('\n')
print('-' * 50)
print('Cod  Nome            Gols              Total')
print('-' * 50)
for i, jogador in enumerate(lista):
    print(f"{i:<4}{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total']}")
print('-' * 50)
print('\n')

while True:
    print('DIGITE 999 PARA SAIR!')
    mostrar_dados = int(input(f'Mostrar dados de qual jogador: '))
    if mostrar_dados == 999:
        break
    if mostrar_dados >= len(lista):
        print(f'ERRO! Não existe jogador com o código {mostrar_dados}. ')
    else:
        print(f" LEVANTAMENTO DO JOGADOR {lista[mostrar_dados]['nome']}: ")
        for i, g in enumerate(lista[mostrar_dados]['gols']):
            print(f'---> No jogo {i + 1} fez {g} gols.')
print('---> VOLTE SEMPRE! <---')

#Aula 20
#Funções - Parte 01
#Funções são vinculadas a palavra - Rotina / Coisas constantes
#Função == def

#Ex.: Função sem parâmetro
def mostra_linha():
    print('-' * 30)

#Depois de usar o comando def dê 2 linhas de distância
mostra_linha()
print('   SISTEMA DE ALUNOS   ')
mostra_linha()
mostra_linha()
print('CADASTRO DE FUNCIONÁRIOS')
mostra_linha()

#Explicando parâmetros
#Ex.: Função com parâmetro
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('SISTEMA DE ALUNOS')

#Ex.: Função com parâmetro
def titulo(txt): #Criamos um parâmetro
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Programa príncipal
titulo('   CURSO EM VIDEO')
titulo('   PYTHON É TOP')

#Ex.: Aula prática
def cauculo(x, y):
    z = x + y
    print(z)


#Programa príncipal
cauculo(4 , 5)
cauculo(8 , 9)
cauculo(2, 1)
cauculo(x=2, y=10)
#-----------------------------------------------------
def soma(x, y):
    print(f'X = {x} e Y = {y}')
    z = x + y
    print(f'A soma X + Y = {z}')


#Programa príncipal
soma(4, 5)
soma(x=15, y=10)
soma(y=5, x=2)

#Empacotar parâmetros
#Ex.:
def contador(* numeros01):# * É o símbolo de desempacotar - Conta quantos números o usuários vai passar
    for valores05 in numeros01:
        print(f'{valores05} ', end='')
    print('FIM!')
    #OU
    tam =len(numeros01)
    print(f'Recebi os valores {numeros01} e são ao todo {tam} números!')
    #Ou
    so = 0
    for valores10 in numeros01:
        so += valores10
    print(f'Somando os valores {numeros01} temos {so}.')

#Programa prícipal
contador(5, 7, 3, 1, 4) #Ele cria uma tupla com esses números
contador(8, 4 , 7)
#------------------------------------------------------

#Agora vamos ver em lista = list()
#Aqui temos 2  lista a: Valores01 e lista01
valores01 = [7, 2, 5, 0, 4]
print(valores01)
def dobra_valores(lista01):
    pos = 0
    while pos < len(lista01):
        lista01[pos] *= 2
        pos += 1


print('Aqui estão os valores dobrados: ', end='')
dobra_valores(valores01)
print(valores01)

#Ex.: Atividade 96 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area_terreno(x, y):
    z = x * y
    print(f'A área de um terreno {x:.1f} x {y:.1f} é de: {z:.1f}m².')


#Programa príncipal
print('---> Controle de terrenos')
print('-' * 25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area_terreno(largura, comprimento)

#Ex. Atividade 97 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(mensagem05):
    tam = len(mensagem05) + 4
    print('-' * tam)
    print(f'  {mensagem05}')
    print('-' * tam)


#Programa Principal
escreva('Mayezer Santana')
escreva('Aprendendo Python')
escreva('Amo Samara! <3')

#Ex.: Atividade 98 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep
def linhas():
    print('=-' * 20)


def fim():
    print('FIM!')


linhas()
print('A contagem de 1 até 10 de 1 em 1:')
sleep(2.0)
for i in range(10):
    print(f'{i + 1}', end= ' ')
    sleep(0.5)
fim()
linhas()
print('A contagem de 10 até 0 de 2 em 2:')
sleep(2.0)
for w in range(10, -1, -2):
    print(f'{w}', end= ' ')
    sleep(0.5)
fim()
linhas()

def contagem_numeros():
    print(f'Contagem de {inicio} até {fim01} de {passo} em {passo}:')
    sleep(2.0)
    if passo > 0:
        for ci in range(inicio, fim01 + 1, passo):
            print(f'{ci}', end= ' ')
            sleep(0.5)
    else:
        for ci in range(inicio, fim01 - 1, passo): #Caso o passo seja um número negativo
            print(f'{ci}', end= ' ')
    fim()


#Programa Principal
print('Agora sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim01 = int(input('Fim: '))
passo = int(input('Passo: '))

if passo == 0: #Evita dar erro caso o passo for 0
    passo = 1

linhas()
contagem_numeros()

#Ex. Atividade 99 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def analise_de_numeros(* numeros10):
    print('==' * 27)
    print('---> Analisando os valores passados...')
    for n00 in numeros10:
        print(f'{n00} ', end= ' ', flush=True) #O parâmetro flush=True dentro de um print() serve para forçar o Python a exibir imediatamente o texto na tela, sem esperar o buffer de saída.
        sleep(0.4)
    print(f'Foram informados {len(numeros10)} valores ao todo.')

    if len(numeros10) > 0:
        print(f'O maior número informado foi:  {max(numeros10)}.')
    else:
        print('Nenhum número foi informado!')
    sleep(1.0)


#Programa principal
analise_de_numeros(2, 9, 4, 5, 7, 1)
analise_de_numeros(4, 7 ,0)
analise_de_numeros(1, 2)
analise_de_numeros(6)
analise_de_numeros()

#Explicando de forma simples:
#Quando o Python imprime algo no terminal, ele normalmente guarda o texto num “buffer” (uma pequena área temporária de memória) e só mostra de fato quando:
#Há uma quebra de linha (\n), ou
#O programa termina, ou
#O buffer “enche”.
#Com flush=True, você diz:
#“Mostra isso na tela agora, sem esperar!”
#flush=False (padrão)	O Python pode guardar a saída temporariamente antes de mostrar.
#flush=True	Obriga o Python a imprimir imediatamente, sem esperar.

#Ex.:
print("Analisando", end=' ')
for ii in range(5):
    print('.', end='', flush=True)  #Mostra o ponto imediatamente
    sleep(0.5)                      #Espera meio segundo
print(" pronto!")

#Ex. Atividade 100 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import sample #Sorteia vários valores únicos de uma lista

numeros = list()
for b in range(1, 11):
    numeros.append(b)
print(f'Lista original: {numeros}')

def sorteio_5_numeros():
    print('==' * 28)
    print('Sorteando 5 valores da lista:', end=' ')
    sorteados = sample(numeros, 5)  #Sorteia 5 valores únicos da lista
    for nav in sorteados:
        print(f'{nav}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    return sorteados  #Devolve os números sorteados


def soma_par(listaas):
    somaas = 0
    for nui in lista:
        if nui % 2 == 0:
            somaas += n
    print(f'Somando os valores pares de {listaas}, temos {soma}.')


# Programa principal
valores = sorteio_5_numeros()
soma_par(valores)

#Aula 21
#Funções - Parte 02

#Assuntos abordados:
#Interactive help, docstrings, Argumentos opcionais, Escopo de variáveis & Retorno de resultados

#Interactive help - Ajuda interativa
help() #Função interna - Um método
#help() - Ele vai explicar para quê serve o comando usado.
#Ex.:
help(print) #Estou vendo para quê serve o print('')
print('Olá Mundo!')

#Maneira alternativa - Funciona +/- igual ao help, nesse caso estou vendo para quê serve o input() e print('')
#Ex.:
print(input.__doc__)
print(print.__doc__)

#DOCSTRINGS
#É uma string de documentação / É um manual de cada comando
#Ex.:
def contador_(iii, fff, ppp):
    """
    ---> Faz uma contagem e mostra na tela.
    :param iii: INICIO DA CONTAGEM
    :param fff: FIM DA CONTAGEM
    :param ppp: PASSO DA CONTAGEM
    :return: SEM RETORNO
    FUNÇÃO CRIADA POR: MAYEZER S. DE SOUZA - ESTUDANTE DE PROGRAMAÇÃO(ENGENHARIA DE SOFTWARE)
    """ #Exemplo de como criar uma DOCSTRINGS
    ciaa = iii
    while ciaa <= fff:
        print(f'{c}', end='..')
        ciaa += ppp
    print('FIM!')


#Programa principal
contador_(2, 10, 2)
help(contador_) #Apemas me mostra os parâmetros
#Para criar um DOCSTRINGS usamos aspas duplas 3 vezes abaixo da função def() criada e faz um manual explicando o que aquela função faz. Exemplo acima ^.
#Então uma DOCSTRINGS serve para 'documentar'(explicar) o que a sua função faz.

#PARÂMETROS OPCIONAIS
#Usamos =0 quando a quantidade de 'valores' solicitados não corresponde com os 'valores' informados.
#Ex.:
def somar_numeros01(aaa, bbb, ccc=0, ddd=0): #Caso
    somas = aaa + bbb + ccc + ddd
    print(f'A soma vale {somas}')


#Programa principal
somar_numeros01(3, 2, 5, 10)
somar_numeros01(8, 4) #Assim o valor de a=8, b=4, c=0 e d=0.
#somar() #Para funcionar precisaria colocar =0 em todos os parâmetros.

#ESCOPO DE VARIÁVEIS OU DE DECLARAÇÕES
#Escopo - É o local onde uma variável vai existir & onde não vai existir.
#Escopo(Variável) global - Posso usar uma variável em quaisquer linha do código.
#Escopo(Variável) local - Somente pode se usada dentro das funções.

#Ex.:
def teste():
    xis = 8 #Essa variável só funciona dentro da função 'teste'. Por tanto não pode ser usada fora da variável. Exemplo lá em baixo.
    print(f'Na função teste, "n" vale {n}.') #Escopo global
    print(f'Na função, "xis" vale {xis}.') #Escopo local


#Programa principal
n = 2 #Escopo global, posso usar em toda a área do código criado.
print(f'No programa principal, "n" vale {n}. ')
teste()
#print(f'No programa principal, "xis" vale {xis}.') - Não funciona, dá erro

#Ex.:
def teste_05(bio): #Parametro formal
    global ar #Significa: Porfavor não crie uma variável'ar', use o 'ar' global
    ar = 8 #Variável local = 8 / Com duas variáveis com o mesmo nome, mas não se misturam
    bio += 4 #Variável local = 9
    cica = 2 #Variável local = 2
    print(f'"A" dentro vale: {ar}')
    print(f'"B" dentro vale: {bio}')
    print(f'"C" dentro vale: {cica}')

ar = 5 #Variável global / Parametro real
teste_05(ar)
print(f'"A" dentro vale: {ar}.') # global ar - Transforma 'ar' local em global = 8

#RETORNO DE VALORES
#As funções podem não retornar, imprimir dentro delas ou retornar um valor = return
#return / Também retorna valor lógico verdadeiro ou falso

#Ex.:
def somar_03(aas=0, bas=0, cas=0):
    somaar_03 = aas * bas + cas
    return somaar_03 #Retorna os valores para uma variável com um novo nome. Exemplo abaixo.


#Programa pricipal
r1 = somar_03(3, 2, 5)
r2 = somar_03(3, 7)
r3 = somar_03(4)
print(f'Meus cálculos deram: {r1}, {r2} e {r3}.')

#PARTE PRÁTICA
#Ex.: Calcular um fatorial de um número e retorna com o programa principal para mostrar na tela
def fatorial(num00=1):
    fator = 1
    for contador00 in range(num00, 0, -1):
        fator *= contador00
    return  fator


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
#Ou
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

#Ex.:
def par(n_=0):
    if n_ % 2 == 0:
        return True
    else:
        return False


#Programa principal
escreva('__PAR OU IMPAR__')
num = int(input('Digite um número: '))
print('\n')
if par(num):
    escreva('É par!')
else:
    escreva('Não é par!')

#Ex.: Atividade 101 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime
def voto(ano_nascimento):
    """
    ---> Determina a situação do voto de uma pessoa com base no ano de nascimento.
    :param ano_nascimento: (int) - O ano de nascimento da pessoa
    :return: (str) - Uma mensagem indicando a idade atual e a situação do voto, podendo ser:
            - "NÃO VOTA" se tiver menos de 16 anos;
            - "VOTO OPCIONAL" se tiver entre 16 e 17 anos ou mais de 70;
            - "VOTO OBRIGATÓRIO" se tiver entre 18 e 70 anos.
    Criado por: Mayezer SS. - Estudante de programação
    """
    atuall = datetime.now().year #Pega o ano atual
    idadee = atuall - ano_nascimento #Subtrai o ano atual pelo ano informado pelo usuário e informa a idade
    if idadee < 16: #Menores de 16 → Não votam.
        print(f'Com {idadee} anos: NÃO VOTA!')
    elif 16 <= idadee < 18 or idadee > 70: #16 e 17 anos ou mais de 70 → Voto opcional.
        print(f'Com {idadee} anos: VOTO OPCIONAL!')
    else: #Entre 18 e 70 → Voto obrigatório.
        print(f'Com {idadee} anos: VOTO OBRIGATÓRIO!')


#Programa principal
print('\n')
print('--' * 15)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
help(voto)
#Ou / Usando return ----------------------------------------------------------------------------------------------------
def voto01(ano_nasci):
    atuall = datetime.now().year
    idaadde = atuall - ano_nasci

    if idaadde < 16:
        return f'Com {idaadde} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idaadde} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idaadde} anos: VOTO OBRIGATÓRIO!'


#Programa principal
ano = int(input('Em que ano você nasceu? '))
resultado = voto01(ano)
print(resultado)

#Ex.: Atividade 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep
def fatorial5(numero_fatorial, show=False): #show (opcional): se for True, a função mostra na tela o processo do cálculo (ex: 5 x 4 x 3 x 2 x 1 =).
    """
    ---> Calcula o fatorial de um número inteiro.
    :param numero_fatorial: (int): O número para o qual o fatorial será calculado.
    :param show: (bool, opcional): Se True, exibe o processo de cálculo passo a passo. O padrão é False.
    :return: (int): O valor do fatorial calculado.
    Exemplo: fatorial15(5) == 120
             fatorial15(5, show=True) == 5 x 4 x 3 x 2 x 1 = 120
    ---> Criado por: Mayezer SS. - Estudante de programação
    """
    fator01 = 1
    for contador001 in range(numero_fatorial, 0 , -1): #Começa do número solicitado até o 0 voltando 1 - Repetição
        if show:
            print(contador001, end= ' ')
            if contador001 > 1: #Quando show= for True, esse bloco será executado — ou seja, vai imprimir o cálculo.
                print(' x ', end= ' ')
                sleep(0.5)
            else: #Quando show= for False, o if não é executado, então nada é mostrado, apenas o valor final é retornado.
                print(' = ', end= ' ')
                sleep(0.5)
        fator01 *= contador001
    return fator01


#Programa principal
print('--' * 17)
n = int(input('Digite um número: '))
print(fatorial5(n, show=True))
print(f'O fatorial de {n} é igual a {fatorial5(n)}')
sleep(2.0)
print('\n')
help(fatorial5)

#Aqui, o show é um parâmetro opcional (também chamado de parâmetro com valor padrão).
#Isso quer dizer que:
#Se você não passar o argumento show ao chamar a função, ele vai valer False por padrão.
#Se você quiser mudar o comportamento, pode passar show=True ao chamar.
#Em outras palavras:
#show=False → a função não mostra o processo, só devolve o resultado.
#show=True → a função mostra o passo a passo do cálculo.
#Pense no show como um interruptor de luz dentro da função:
#show=False → luz apagada → função só trabalha internamente, sem mostrar nada.
#show=True → luz acesa → função mostra o que está fazendo passo a passo.

#Ex.:
def potencia(base, expoente, show=False):
    """
    Calcula a potência de um número, opcionalmente mostrando o processo.
    Parâmetros:
        base (int ou float): O número base.
        expoente (int): O expoente.
        show (bool, opcional): Se True, mostra a multiplicação passo a passo.
    Retorna:
        int ou float: O resultado da potência.
    """
    resultado002 = base ** expoente
    if show:
        print(' x '.join([str(base)] * expoente), '=', resultado002)
    return resultado002


#Programa principal
print(potencia(3, 4))
# Saída: 81
print(potencia(3, 4, show=True))
# Saída: 3 x 3 x 3 x 3 = 81

#Ex.: Atividade 103 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha_jogador(jogadorr='<desconhcido>', gol=0):
    print(f'O jogador {jogadorr} fez {gol} gol(s) no campeonato.')


#Programa principal
print('--' * 27)
nome_jogador = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: ')).strip()
if gols.isnumeric(): #Transforma string em int(número(valor)) inteiro
    gols = int(gols)
else: #Se tiver em branco da igual a 0
    gols = 0
if nome_jogador.strip() == '': #Se estiver vazio ==
    ficha_jogador(gol=gols)
else:
    ficha_jogador(nome_jogador, gols)

#Ex.: Atividade 104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')
def leia_int(numero_int):
    while True:
        numeror = str(input(numero_int))
        if numeror.isnumeric():
            print(f'Você acabou de digitar o número {numeror}')
            return numeror
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')



#Projeto principal
print('--' * 27)
valor = leia_int('Digite um número: ')

#Ex.: Atividade 105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)
#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(valor_01, valor_02, valor_03, valor_04, sit=False): #Pode se usar *valor_, para não criar somente 4 variáveis
    """
    ---> Função para receber notas de alunos e retornar um dicionário com:
         QUANTIDADE DE NOTAS, MAIOR NOTA, MENOR NOTA, MÉDIA DA TURMA & (OPCIONAL)SITUAÇÃO DA TURMA.

    :param valor_01: float(5.5) - 1° Nota
    :param valor_02: float(9.5) - 2° Nota
    :param valor_03: float(10) - 3° Nota
    :param valor_04: float(6.5) - 4° Nota
    :param sit: bool - Se True, adiciona a situação da turma ao retorno
    :return: dict com os dados das notas

    ---> Criado por: Mayezer SS. - ESTUDANTE DE PROGRAMAÇÃO/Engenharia de Software
    """
    listaaa = [valor_01, valor_02, valor_03, valor_04]
    dicionariooo = dict()

    dicionariooo['total'] = len(listaaa)
    dicionariooo['maior'] = max(listaaa)
    dicionariooo['menor'] = min(listaaa)
    mediaaa = (valor_01 + valor_02 + valor_03 + valor_04) / 4
    dicionario['media'] = mediaaa #Pode ser usado assim também: resultado['media'] = sum(notas) / len(notas)

    if sit:
        if dicionariooo['media'] < 6:
            dicionariooo['situação'] = 'RUIM'

        elif dicionariooo['media'] < 8:
            dicionariooo['situação'] = 'BOA'

        else:
            dicionariooo['situação'] = 'EXCELENTE'

    return dicionariooo


#Programa principal
resposta = notas(5.5, 9.5, 10, 6.5, sit=True) #Pode remover sit=True
print(resposta)
print('\n')
help(notas)

#Ex. Atividade 106 Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
from time import sleep
cores = {'limpa': '\033[m',
         'fundo_verde': '\033[7;32m',
         'fundo_azul': '\033[7;34m',
         'fundo_branco': '\033[7;37m',
         'fundo_vermelho': '\033[7;31m'}

def linhas_apresentacao():
    """---> Faz uma apresentação sobre o programa com um sistema cor: Fundo verde
    :return: print('')

    Exemplo: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     SISTEMA DE AJUDA PyHELP
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(f"{cores['fundo_verde']}~~{cores['limpa']}" * 20)
    mensagemm = 'SISTEMA DE AJUDA PyHELP'
    print(f"{cores['fundo_verde']}{mensagemm:^40}{cores['limpa']}")
    print(f"{cores['fundo_verde']}~~{cores['limpa']}" * 20)


#Programa principal
while True:
    linhas_apresentacao()
    funcao_biblioteca = str(input('Função ou Biblioteca: ')).strip().lower()
    print('\n')

    if funcao_biblioteca == '': #Quando deixa em branco, para não dar erro cai aqui.
       print(f"{cores['fundo_azul']}PROCURANDO O COMANDO {funcao_biblioteca}... {cores['limpa']}")
       sleep(1.0)
       print(f'{cores['fundo_branco']}')
       help(funcao_biblioteca)
       print(f"{cores['limpa']}")
       print('\n')

    elif funcao_biblioteca == 'fim': #Quando digita 'fim' cai aqui
        print(f"{cores['fundo_vermelho']} FINALIZANDO...{cores['limpa']}")
        sleep(0.8)
        print(f"{cores['fundo_vermelho']}ATÉ LOGO!{cores['limpa']}")
        break

    else:
        print(f"{cores['fundo_azul']}PROCURANDO O COMANDO {funcao_biblioteca}... {cores['limpa']}")
        sleep(1.0)
        print(f'{cores['fundo_branco']}') #Quando o usuário digita qualquer coisa cai aqui
        help(funcao_biblioteca)
        print(f"{cores['limpa']}")
        print('\n')


#Aula 22 ------------------------------------------------------------
#Módulos e Pacotes

#Modularização - Criar módulos
#Surgiu na década de 60 - Sistemas ficando cada vez maiores
#Foco 01: principal: Dividir um programa grande
#Foco 02: Aumentar a legibilidade
#Foco 03: Facilitar a manutenção
#Vamos utilizar módulos para transformar um problemão em pequenos problemas

#Ex.
def factorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):                   #Posso criar um arquivo "uteis.py", e ficam salvo as funções
    return  n * 2               #Para chamar esse arquivo, podemos chamar usando - import
                                #Então ficaria "import uteis" - Fazendo assim uma modularização
                                #fat = uteis.factorial(num) - Utlizando o módulo
def triplo(n):                  #int(f'O dobro de {num} é {uteis.dobro(num)}')
    return n * 3                #print(f'O triplo de {num} é {uteis.triplo(num)}')
                                #Ou chama as funções diretas, usando "from" - Porém não é recomendado

num = int(input('Digite um valor: '))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

#Vantagens de ter uma modularização ------------------
#Organização do código
#Facilidade na manutenção
#Ocultação de código detalhado
#Reutilização em outros projetos - Só copiar o arquivo

#Pacotes ou em outras linguagens "bibliotecas"
#Podemos separar por assuntos as funções
#Tipo: Funções somente para números, ou para strings, e até mesmo para datas e cores
#Usando: "from uteis import datas"
#Para criar um pacote, podemos simplismente dentro da pasta uteis, criamos outras pastas e dentro das pastas criaremos um arquivo .py chamado: __init__.py
#Na hora de criar o pacote, teremos a opção: Python Package
#Podendo criar pacotes dentro de outros pacotes


#Aula 23 ---------------------------------------------------------------------
#Tratamento de Erros e Exceções
#Usamos "try:" - tente fazer alguma coisa
#Usamos "exept:" - se não, tente isso

#Ex.
#try: - Tentar
    #operação
#except: - Se der erro
    #falhou

#Claasulas opcionais
#else: - Se der certo
    #deu certo
#finally: - Finalmente / Vai acontecer independente se deu certo ou se der erro
    #certo/falha

#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:
    print('Infelizmente tivemos um problema!')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')

#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')

#O "try:" pode ter vários "except:"
#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')

#Ex. Atividade 113 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'pretoebranco': '\033[7;30m'}
while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
        real = float(input('Digite um número real: '))

    except:
        print(f"{cores['vermelho']}ERRO: Por favor, digite um número inteiro válido!{cores['limpa']}")

    else:
        print(f"{cores['azul']}O valor inteiro foi {inteiro} e o real foi {real:.1f}{cores['limpa']}")

#Ex. Atividade 114 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read()) #Me da o código HTML do site inteiro







