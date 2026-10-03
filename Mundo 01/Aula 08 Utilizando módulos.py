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