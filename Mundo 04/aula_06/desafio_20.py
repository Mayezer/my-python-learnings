# DESAFIO 020: Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.

from rich import print
from time import sleep


class Gamer():

    def __init__(self):
        self.nick = input("Qual o seu nick: ").capitalize()
        self.jogos_favoritos = input("Quais são seus jogo preferidos: ").capitalize()
        

