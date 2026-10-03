#Aula 06
#(int), (float), (bool) e (str).
#(int) Números inteiros: Ex. 2, -8, 0 ou até mesmo 9586.
#(float) Números ponto flutuante(números reais): Ex. 5.5, 0.086, 7.0 ou até mesmo -15.654.
#(bool) Valor boleano, que só aceita dois valores, sempre começando com letra maiúscula: Ex. True ou False(Verdadeiro ou Falso)
#(str) São palavras, sempre entre aspas. Ex. 'Olá', '7.2' ou até mesmo aspas vazias, ''.

#Ex.05 atividade 003
#n1 = Número 01
#n2 = Número 02
n1 = int(input ('Primeiro número: '))
n2 = int(input ('Segundo número: '))

print ('A Soma é: ', n1 + n2)

#Tipo primitivo

#Ex.06
#n01 = Número 01
n01 = input('Digite um valor: ')
print (type(n01))

#Ex.07
#n02 = Número 01
n02 = int(input('Digite um valor: '))
print (type(n02))

#Ex.08
#n03 = Número 01
#n04 = Número 02
n03 = int(input ('Primeiro número: '))
n04 = int(input ('Segundo número: '))
soma = n03 + n04

print ('A Soma é: ', soma)

#Quando se junta uma string na outra, se chama: Concatenação

#Ex.09
#n05 = Número 01
#n06 = Número 02
n05 = int(input ('Primeiro número: '))
n06 = int(input ('Segundo número: '))
soma = n03 + n04

print ('A Soma entre: ', n05, ' e ', n06, 'é: ', soma)

#Chaves {} se chama mascara.
#(format) serve para dar certos valores.

#Ex.10
#n07 = Número 01
#n08 = Número 02
n07 = int(input ('Primeiro número: '))
n08 = int(input ('Segundo número: '))
soma = n07 + n08
# print ('A Soma entre: ', n07, ' e ', n08, 'é: ', soma)
print ('A soma entre {} e {} vale: {}'.format(n07, n08, soma))

#Outra forma de escrever
#n4 = Número 01
#n5= Número 02
n4 = int(input ('Primeiro número: '))
n5 = int(input ('Segundo número: '))
calculo = n4 + n5
print (f'A soma de {n4} e {n5} é {calculo}')

#Ex.11
num = float(input('Digite um valor: '))
print(num)
#7.0

num01 = str(input('Digite um valor: '))
print(num01)
#7

num02 = bool(input('Digite um valor: '))
print(num02)
#Se responder um número vira True(Verdadeiro), e se só apertar enter vira False(Falso).

num03 = (input('Digite um valor: '))
print(num03.isnumeric())
#(isnumeric) vai dizer se é possivel converter esse valor no momento em um número com o tipo primitivo int antes dele.
#3 = True Porque é número.
#3a = False Porque não é número.

num04 = (input('Digite um valor: '))
print(num04.isalpha())
#(isalpha) se é letra.
#www = True Porque só tem letras.
#123 = Falso Porque é números.

num05 = (input('Digite um valor: '))
print(num05.isalnum())
#(isalnum) è alfanúmerico Alfabeto e Númerico.
#6, 3a ou 0i = São True, por terem números e letras.
#( ) Espaço é False.

num06 = (input('Digite um valor: '))
print(num06.isupper())
#Serve para saber se só tem letras maiúculas.
#E etc.. Existem vários métodos de testes de tipos.

#Ex.12 Atividade 004
tipo1 = input('Me diz algo ai: ')

print('O tipo primitivo desse valor é: ', type(tipo1))
print('É maiúscula:', tipo1.isupper())
print('É alfabético: ', tipo1.isalpha())
print('É alfanúmerico: ', tipo1.isalnum())
print('É um número:', tipo1.isnumeric())
print('É um espaço em branco: ', tipo1.isspace())
print('É um decimal: ', tipo1.isdecimal())
print('É minúcula:', tipo1.islower())
