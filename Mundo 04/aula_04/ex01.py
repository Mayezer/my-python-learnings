# Declaração da classe
class Aluno:

    def __init__(self): # Método mágico, método construtor ou dunder init.
        self.nome = "" # Então self é um nome genérico de um atributo de instância.
        self.idade = 0 # A idade de si próprio / self() é ele mesmo. Resumindo ele passa a propriedade dele para o objeto.
        self.curso = ""

    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f"{self.nome} é aluno de {self.curso} e tem {self.idade} anos de idade."


# Declaração de Objetos
aluno01 = Aluno() # aluno01 é o obejto e Aluno() é a minha classe e os () é a chamada para o método.
# Esse obejto 'aluno01' é justamente um nome genérico para o self, self é si próprio.
aluno01.nome = "Mayezer" # Não tem prarênteses é atributo.
aluno01.curso = "Egenharia de Software"
aluno01.idade = 26 # Po lá em cima ter o self, aqui i objeto aluno01, vira o self de cima, passando o parâmetro para 'idade = 26'.
aluno01.aniversario() # Tem parênteses no final, é método.

print(aluno01)


aluno02 = Aluno() # Um novo objeto, feito do mesmo molde (classe).
aluno02.nome = "Samara"
aluno02.curso = "Medicina"
aluno02.idade = 27
aluno02.aniversario() # Aqui chamamos a mesma função, porém em uma instância diferente
# Tendo isso em mente, podemos ter quantos objetos quiser, usando a mesma classe

print(aluno02)


# ----------------------------------------------------------------------------------------

# Para fixar: Você pode jogar essa classe em um arquivo “solto” somente para essas classes (funções), podendo assim, só importar em algum outro momento em algum outro arquivo dentro do projeto.
