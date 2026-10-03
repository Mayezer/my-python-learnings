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

#HUBLA
contador = 0
while contador < 10 + 1:
    print(contador)
    contador += 1


