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