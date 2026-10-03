# DESAFIO 019: Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.

from time import sleep
from rich import print


class Livro():

    def __init__(self):
        self.nome_livro = input("Qual o nome do livro: ").capitalize()
        while True:
            try:
                self.paginas = int(input("Quantas páginas ele terá: "))
                break
            except:
                print("Digite um NÚMERO inteiro!")
                continue
        print(f"\nVocê acabou de abrir o livro {self.nome_livro} que tem {self.paginas} páginas no total! \nVocê agora está na página: 1 \n")
        while True:
            try:
                self.prox_pagina = int(input("Quantas páginas você deseja avançar: "))
                break
            except:
                print("Digite um NÚMERO inteiro!")
                continue

    def passar_pagina(self):
        while True:
            if self.paginas >= self.prox_pagina:
                for i in range(self.prox_pagina):
                    print(f"Página.{i + 2}", end= " ")
                    sleep(0.5)
                print(f"\nVocê avançou {self.prox_pagina} páginas e agora está na página {self.prox_pagina + 1}")
                break
            else:
                print(f"\nSeu livro só tem {self.paginas} PÁGINAS! \nVocê está delirando de tanto ler, vá descansar! XD")
                break


leitor = Livro()
leitor.passar_pagina()
