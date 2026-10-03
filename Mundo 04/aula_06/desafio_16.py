# DESAFIO 016: Crie a classe Funcionário, onde podemos cadastrar nome, setor e cargo. Crie também método que permita ao funcionário se apresentar.
from rich import print


class Funcionario():
    """
        Cadastra um funcionário com seu setor e cargo e pode-se fazer uma apresentação dele
    """

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome} | Setor: {self.setor} | Cargo: {self.cargo}"

    def apresentacao(self):
        return f"Olá, me chamo {self.nome} sou do setor {self.setor} e meu cargo é {self.cargo}!"


funcionario01 = Funcionario("Mayezer", "Tecnológico", "Engenheiro de Software")
print(funcionario01)
print(funcionario01.apresentacao())
