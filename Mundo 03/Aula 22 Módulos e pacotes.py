#Aula 22 ------------------------------------------------------------
#Módulos e Pacotes

#Modularização - Criar módulos
#Surgiu na década de 60 - Sistemas ficando cada vez maiores
#Foco 01: principal: Dividir um programa grande
#Foco 02: Aumentar a legibilidade
#Foco 03: Facilitar a manutenção
#Vamos utilizar módulos para transformar um problemão em pequenos problemas

#Ex.
def factorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(n):                   #Posso criar um arquivo "uteis.py", e ficam salvo as funções
    return  n * 2               #Para chamar esse arquivo, podemos chamar usando - import
                                #Então ficaria "import uteis" - Fazendo assim uma modularização
                                #fat = uteis.factorial(num) - Utlizando o módulo
def triplo(n):                  #int(f'O dobro de {num} é {uteis.dobro(num)}')
    return n * 3                #print(f'O triplo de {num} é {uteis.triplo(num)}')
                                #Ou chama as funções diretas, usando "from" - Porém não é recomendado

num = int(input('Digite um valor: '))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')

#Vantagens de ter uma modularização ------------------
#Organização do código
#Facilidade na manutenção
#Ocultação de código detalhado
#Reutilização em outros projetos - Só copiar o arquivo

#Pacotes ou em outras linguagens "bibliotecas"
#Podemos separar por assuntos as funções
#Tipo: Funções somente para números, ou para strings, e até mesmo para datas e cores
#Usando: "from uteis import datas"
#Para criar um pacote, podemos simplismente dentro da pasta uteis, criamos outras pastas e dentro das pastas criaremos um arquivo .py chamado: __init__.py
#Na hora de criar o pacote, teremos a opção: Python Package
#Podendo criar pacotes dentro de outros pacotes

