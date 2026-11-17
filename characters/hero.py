from characters.character import Character
import pygame

class Hero(Character):

    def __init__(self, position: list[int], position_change: list[int], sprite: str):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position, sprite, position_change)

    def move_limitations(self, limitation=736):
        """
        Permet à l'héro de rester dans le cadre du jeu s'il dépasse soit la valeur x ou y du cadre du jeu
        """

        self.position[self.X] += self.position_change[self.X]
        if self.position[self.X] <= 0:
            self.position[self.X] = 0
        elif self.position[self.X] >= limitation:
            self.position[self.X]= limitation

    def handle_moves(self, event, vitesse= 5):
        """
        Cette fonction permet de gérer les mouvements du héro dans le cadre du jeu
        :param vitesse: la vitesse qui est mis à 5 par défaut
        :param event: un évènement d'utilisateur d'appuyer sur une des flèches suivantes
        [UP, RIGHT, LEFT ]
        """
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.position_change[self.X] = - vitesse
            if event.key == pygame.K_RIGHT:
                self.position_change[self.X] = vitesse

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.position_change[self.X] = 0