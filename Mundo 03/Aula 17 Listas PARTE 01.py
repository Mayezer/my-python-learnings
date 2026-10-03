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
