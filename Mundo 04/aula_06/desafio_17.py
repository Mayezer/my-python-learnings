# DESAFIO 017: Crie a classe Produtos, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from time import sleep


class Produto():

    def __init__(self, nome = "", preco = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}"

    def etiqueta(self):
        return f"{self.nome} ----> R$ {self.preco:.2f}"

produto01 = Produto("Lapiz", 2.30)
produto02 = Produto("Borracha", 5.50)
produto03 = Produto("Caneta", 8.50)
print(f"\nNossos produtos: {produto01}, {produto02}, {produto03}")

print(f'Qual produto você deseja ver o preço? \n(1) \n(2) \n(3) \n')
while True:
    try:
        produtos = int(input('(Digite 999 para sair) \n1, 2 ou 3: '))
    except ValueError:
        print("Não aceitamos letras ou caracteres. ESCOLHA: 1, 2 ou 3! \n")
        continue

    if produtos == 1:
        print("Processando...")
        sleep(1)
        print(f'{produto01.etiqueta()} \n')
        sleep(2)
    elif produtos == 2:
        print("Processando...")
        sleep(1)
        print(f"{produto02.etiqueta()} \n")
        sleep(2)
    elif produtos == 3:
        print("Processando...")
        sleep(1)
        print(f"{produto03.etiqueta()} \n")
        sleep(2)
    elif produtos == 999:
        print("Finalizando...")
        sleep(1)
        print("Finalizado! Obrigado por fazer parte desse teste.")
        break
    else:
        print("\nNúmero INVÁLIDO!\n")
        sleep(1)
        continue

# print(f"{produto01.etiqueta()}, \n{produto02.etiqueta()}, \n{produto03.etiqueta()}")
