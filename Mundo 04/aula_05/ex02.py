from rich import print


# Declaração de Classe
class Pessoa:
    """
        Essa classe cria uma Pessoa, que tem nome e idade.
        Para criar uma nova pessoa, use:
        variavel = Pessoa(nome, idade)
    """

    def __init__(self, nome = "", idade = 0): #Método construtor, Se eu não informar o valor de 'nome' ou 'idade', ele se auto encrementa com valor vazio em 'nome' e valor 0 em 'idade '.
        # Atributos de Instância
        self.nome = nome # Nesse caso 'nome' recebe o valor de 'nome'.
        self.idade = idade #Nesse caso 'idade' recebe o valor de 'idade'.

    # Métodos de Instância
    def aniversario(self): #
        self.idade = self.idade + 1

    def __str__(self): # Todo objeto já tem um método str, ele mostra o endereço do objeto na memória. Porém podemos editar esse método.
        return f"{self.nome} é umaclear Pessoa e tem {self.idade} anos de idade."

    def __getstate__(self): # Podemos programar um estado
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
g1 = Pessoa("Mayezer", 26) # 
g1.aniversario()
print(g1)

g2 = Pessoa("Samara", 27) # 
print(g2)

g3 = Pessoa("Vazio") # 
g3.aniversario()
print(g3)

print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Método

print(g1.__class__) # Para saber qual a classe desse objeto. 

print(int.__doc__) # Faz um atributo, é um dunder attribute ou um atributo com duplo underline __. Nesse caso, vai me retornar uma explicação do que é int.
