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
