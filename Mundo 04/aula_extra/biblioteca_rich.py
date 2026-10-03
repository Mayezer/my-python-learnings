from rich import print # Adiciona funcionalidades novas e úteis para o print convencional.

print("Olá,[red] Mundo[/] :earth_americas:!")
print("Olá, [bold blue on white]Pequeno Gafanhoto[/] :Vulcan_salute:")

# ----------------------------------------------------------------------------------------

from rich.panel import Panel # Cria um painel

caixa = Panel("[white]Esse aqui é um painel de exemplo[/]", title="Mensagem", style="red")
print(caixa)

# ----------------------------------------------------------------------------------------

from rich.table import Table # Cria uma tabela

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="center", style="red")
tabela.add_column("Preço" , justify="center", style="blue")
tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "[green]R$5,00[/]")

print(tabela)

# ----------------------------------------------------------------------------------------

from rich import inspect # Nos retorna uma explicação detalhada e organizada da classe, função... que pedirmos.

print(int.__dict__) # Irá organizar todo o retorno.

inspect(int, all=True) # all=True retorna todas as formas para usarmos.

# ----------------------------------------------------------------------------------------

from rich.traceback import install # Todo erro que tivermos no código, ele vai monitorar e informar de uma forma visual mais limpa e fácil de entender.
install() # Chamamos a função antes do código.

def divisão(x, y):
	return x / y

print(divisão(50, 0))

# ----------------------------------------------------------------------------------------

# Acessando o site: rich.readthedocs.io | Teremos a documentação dessa biblioteca.
# Para instalar a biblioteca no terminal: pip install rich
# No terminal, use: python3 –m rich.emoji | Irá nos retornar todos os comandos dos emojis da biblioteca. 