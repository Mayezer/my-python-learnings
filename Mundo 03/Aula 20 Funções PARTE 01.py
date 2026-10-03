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
