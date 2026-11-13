from characters.character import Character
import pygame
from pygame import mixer

class Hero(Character):

    def __init__(self, position: list[int],position_change: list[int], sprite: str, nombre_vies: int):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position,sprite, position_change, nombre_vies)

    def fire(self):
        pass

    def move(self, screen):
        pass