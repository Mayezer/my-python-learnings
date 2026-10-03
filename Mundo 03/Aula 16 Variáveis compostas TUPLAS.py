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