#Aula 23 ---------------------------------------------------------------------
#Tratamento de Erros e Exceções
#Usamos "try:" - tente fazer alguma coisa
#Usamos "exept:" - se não, tente isso

#Ex.
#try: - Tentar
    #operação
#except: - Se der erro
    #falhou

#Claasulas opcionais
#else: - Se der certo
    #deu certo
#finally: - Finalmente / Vai acontecer independente se deu certo ou se der erro
    #certo/falha

#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:
    print('Infelizmente tivemos um problema!')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')

#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')

#O "try:" pode ter vários "except:"
#Ex.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')

#Ex. Atividade 113 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m'}
while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
        real = float(input('Digite um número real: '))

    except:
        print(f"{cores['vermelho']}ERRO: Por favor, digite um número inteiro válido!{cores['limpa']}")

    else:
        print(f"{cores['azul']}O valor inteiro foi {inteiro} e o real foi {real:.1f}{cores['limpa']}")

#Ex. Atividade 114 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read()) #Me da o código HTML do site inteiro
