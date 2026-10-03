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
