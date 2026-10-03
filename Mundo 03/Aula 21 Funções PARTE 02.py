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
