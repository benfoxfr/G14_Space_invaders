from characters.character import Character
import pygame

class Hero(Character):

    def __init__(self, position: list[int],position_change: list[int], sprite: str, nombre_vies: int):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position,sprite, position_change, nombre_vies)


    def move_limitations(self, X, Y):
        """
        Permet à l'héro de rester dans le cadre du jeu si il dépasser soit la valeur x ou y du cadre du jeu
        """

        self.get_position[X] += self.get_position_change[X]
        if self.get_position[X] <= 0:
            self.set_positionX(0)
        elif self.get_position[X] >= 736:
            self.set_positionX(736)

    def handle_moves(self,event):
        """
        Cette fonction permet de gérer les mouvements du héro dans le cadre du jeu
        :param event: un évènement d'utilisateur d'appyer sur une des flèches suivantes
        [UP, RIGHT, LEFT ]
        """


        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.set_positionX(-5, position_change=True)
            if event.key == pygame.K_RIGHT:
                self.set_positionX(5, position_change=True)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.set_positionX(0, position_change=True)