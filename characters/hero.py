from characters.character import Character
from characters.bullet import Bullet
import pygame
from pygame import mixer

# con
GAME_OVER = "Game over !"
CONTINUE = "Continer le jeu !"

class Hero(Character, Bullet):

    def __init__(self, positionX: int, positionY: int, sprite: str, characterX_change: int, nombre_vies):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(positionX, positionY, sprite, characterX_change,nombre_vies)


    def fire(self):
        pass
