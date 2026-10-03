# DESAFIO 018: Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

from rich import print
kg_carne = 82.40

class Churrasco:

    def __init__(self):
        self.nome = str(input("Qual o nome do churrasco: "))
        self.convidados = int(input("Quantas pessoas virão: "))
        self.carne_por_pessoa = 0.4
        self.total_carne = self.carne_por_pessoa * self.convidados
        self.custo_total = self.total_carne * kg_carne
        self.custo_por_pessoa = self.custo_total // self.convidados

    def __str__(self):
        return f"""
Analizando {self.nome} com {self.convidados} convidados.
Cada participante comerá {self.carne_por_pessoa}kg e cada kg custa R$ {kg_carne:.2f} 
Recomendo comprar {self.total_carne:.3f}kg de carne
O custo total será de R${self.custo_total:.2f}
Cada pessoa pagará R$ {self.custo_por_pessoa:.2f} para participar!
                """

churrasco01 = Churrasco()
print(churrasco01)
