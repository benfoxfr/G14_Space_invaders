from characters.character import Character
import pygame
from pygame import mixer

class Hero(Character):

    def __init__(self, position: list[int], sprite: str, characterX_change: int, nombre_vies: int):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position, sprite, characterX_change, nombre_vies)

    def fire(self):
        pass

    def move(self, screen):
        pass