from characters.character import Character
from characters.bullet import Bullet
import pygame
from pygame import mixer

# con
GAME_OVER = "Game over !"
CONTINUE = "Continer le jeu !"

class Hero(Character, Bullet):

    def __init__(self, position: list[int], sprite: str, characterX_change: int, nombre_vies: int):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position, sprite, characterX_change, nombre_vies)


    def fire(self):
        pass
