from pygame.event import Event
from entities.entity import Entity
import pygame


class Hero(Entity):

    def __init__(self, position: list[int], position_change: list[int], sprite: str):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position, sprite, position_change)

    def move_limits(self, limitation=736) -> None:
        """
        Garde le héro dans le cadre du jeu lors de son déplacement  (appel à la fonction move)

        :param limitation: la limite max en position X du cadre du jeu
        """
        self.position[self.X] += self.position_change[self.X]
        if self.position[self.X] <= 0:
            self.position[self.X] = 0
        elif self.position[self.X] >= limitation:
            self.position[self.X] = limitation

    def move(self, event: Event, speed=5) -> None:
        """
        Déplace le héro dans le cadre du jeu

        :param event: l'action réalisée par le héro parmi les suivantes
        [Aller à droite, Aller à gauche, ne rien faire]
        :param speed: la vitesse par défaut qui est 5 d'une instance Hero
        """
        # La gestion des touches utilisateurs pour se déplacer
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.position_change[self.X] = -speed
            if event.key == pygame.K_RIGHT:
                self.position_change[self.X] = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.position_change[self.X] = 0
