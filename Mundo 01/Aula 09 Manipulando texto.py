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