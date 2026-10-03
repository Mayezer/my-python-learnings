#Aula 07
#Operações aritméticas.
#(+) Adição, (-) Subtração, (*) Multiplicação, (/) Divisão, (**) Potência(raiz quadrada), (//) Divisão Inteira e (%) Resto da Divisão.
#(==) Significa igual.

#5 + 2 == 7
#5 - 2 == 3
#5 * 2 == 10
#5 / 2 == 2.5
#5 ** 2 == 25
#5 // 2 == 2
#5 % 2 == 1

#Ordem das operações: 1° - (), 2° - **, 3° - *, /, // e %, 4° - + e -.

#Ex.13
#5 + 3 * 2 == 11
#3 * 5 + 4 ** 2 == 31
#3 * (5 + 4) ** 2 == 243
#oi * 5 == oioioioioi

#Ex.14
#{:=^20}, {:<20}, {:>20}
nome = input('Qual o seu nome?')
print(f'Prazer em conhecer você {nome:=^20}!')
#Qual o seu nome? Mayezer
#Prazer em conhecer você ======Mayezer=======!

#Ex.15
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é: {}, \n O produto é: {} \n Divisão é: {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é: {} e potência é: {}'.format(di,e))

#(\n) Serve para cortar textos, (quebrar).
#(end=' ') Serve para tudo finalizar na mesma linha. Sendo vazio ou não.

#Ex.16 Atividade 005 - Enunciado: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
n1 = n - 1
n2 = 1 + n

print('Analisando o valor: {}, seu antecessor é: {} e o sucessor é: {:/^10}'.format(n, n1, n2, end=' '))

#Ex.17 Atividade 006 - Enunciado: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
teste = int(input('Insira seu número: '))
dobro = 2 * teste
triplo = 3 * teste
raiz = teste ** 0.5

print('O dobro de {} é: {} , \n O triplo de {} é: {}, \n A raiz quadrada de {} é: {:.3f}'.format(teste, dobro, teste, triplo, teste, raiz))

#Ex.18 Atividade 007 - Enunciado: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
teste1 = float(input('Primeira nota do aluno: '))
teste2 = float(input('Segunda nota do aluno: '))
teste3 = (teste1 + teste2) / 2

print('A média entre {} e {} é igual a {}'.format(teste1, teste2, teste3))

#Ex.19 Atividade 008 - Enunciado: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Uma distância em metros: '))
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a: \n {}cm \n {}mm'.format(m, cm, mm))

#Ex.20 Atividade 009 - Enunciado: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
tabuada = int(input('Me fale um número, e eu te falo a tabuada de multiplicação: '))
n0 = 0 * tabuada
n1 = 1 * tabuada
n2 = 2 * tabuada
n3 = 3 * tabuada
n4 = 4 * tabuada
n5 = 5 * tabuada
n6 = 6 * tabuada
n7 = 7 * tabuada
n8 = 8 * tabuada
n9 = 9 * tabuada
n10 = 10 * tabuada

print(f'0 x {tabuada} igual a: {n0}')
print(f'1 x {tabuada} igual a: {n1}')
print(f'2 x {tabuada} igual a: {n2}')
print(f'3 x {tabuada} igual a: {n3}')
print(f'4 x {tabuada} igual a: {n4}')
print(f'5 x {tabuada} igual a: {n5}')
print(f'6 x {tabuada} igual a: {n6}')
print(f'7 x {tabuada} igual a: {n7}')
print(f'8 x {tabuada} igual a: {n8}')
print(f'9 x {tabuada} igual a: {n9}')
print(f'10 x {tabuada} igual a: {n10}')

#Ex.21 Atividade 010 - Enunciado: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1.00 = R$ 6.25
cart = float(input('Quanto de dinheiro você tem na carteira: R$'))
dolar = cart / 6.5

print(f'Com R${cart} você pode comprar: US${dolar:.2f}')

#Ex.22 Atividade 011 - Enunciado: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
m2 = lar * alt
tinta = m2 / 2

print(f'Sua parede tem uma dimensão de {lar}x{alt} e sua área é de: {m2}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}L de tinta.')

#Ex.23 Atividade 012 - Enunciado: Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
pre = float(input('Qual o preço do produto: R$'))
desc = pre * 0.05
val = pre - desc

print(f'O preço do produto é: R${pre}.\nO desconto de 5% é: R${desc}.\nE o valor com desconto é: R${val}')

#Ex.24 Atividade 013 - Enunciado: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual é o salário do Funcionário: R$'))
mult = sal * 0.15
aum = sal + mult

print(f'Um funcionário que ganhava R${sal:.2f}, com 15% de aumento, irá receber: R${aum:.2f}.')

#Ex.25 Atividade 014 - Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c1 = float(input('Informe a temperatura em °C: '))
f1 = (c1 * 1.8 + 32) #Também da para fazer: f1 = ((9 * c1) / 5 + 32)

print(f'A temperatura em °C é: {c1:.1f}°C (Celsius), que corresponde a: {f1:.1f}°F (Fahrenheit).')

#Ex.26 Atividade 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = float(input('Quantos dias alugados: '))
km = float(input('Quantos KM rodados: '))

c1 = dia * 60
c2 = km * 0.15
c3 = c1 + c2

print(f'O valor de dias alugados é: R${c1:.2f}\nO valor de KM rodados é: R${c2:.2f}\nO valor total a se pagar é: R${c3:.2f}')
