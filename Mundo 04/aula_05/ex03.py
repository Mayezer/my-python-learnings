from rich import print


class ContaBancaria():
    """
        Cria uma conta bancária e permite fazer saques e depósitos
        Variavel = ContaBancaria(111, "NOME DA PESSOA", 3000)
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo!"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self.id}!")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO! Saque de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado na conta {self.id}!")


conta01 = ContaBancaria(111, "Mayezer", 3000)
conta01.depositar(1000)
print(conta01)
conta01.sacar(500)
print(conta01)


# ----------------------------------------------------------------------------------------

# Acesse o site: peps.python.org / E entenda melhor sobre PEPs (Python Enhancement Proposals) resumindo, são algumas “regras” na hora de escrever códigos em python. 
# Sempre documente suas docstrings/classes.
