from abc import abstractmethod

import pygame


class Entity:
    def __init__(self, position: list[int], sprite: str, position_change: list[int]):
        if len(position) != 2:
            raise ValueError(f"La liste {position} doit contenir la position [x, y]")
        self.position = position
        self.sprite = sprite
        if len(position_change) != 2:
            raise ValueError(f"La liste {position_change} doit contenir la position [x, y]")
        self.position_change = position_change
        self.X = 0
        self.Y = 1

    @property
    def get_sprite(self):
        """
        retourne la source image
        """
        return self.sprite

    @property
    def get_position(self):
        """
        Retourne la position
        """
        return self.position

    @property
    def get_position_change(self):
        """
        retourne la vitesse de déplacement
        """
        return self.position_change

    @property
    def load_sprite(self):
        """
        Charge le sprite
        """
        return pygame.image.load(self.sprite)

    def set_positionX(self, new_position: int, position_change=False) -> None:
        """
        Modifie la position ou sa vitesse, mais seulement en X.

        :param new_position: La nouvelle position ou vitesse
        :param position_change: Booléen, s'il est True change la vitesse
        :return: Change la position ou sa vitesse de déplacement.
        """
        if position_change:
            self.position_change[self.X] = new_position
        else:
            self.position[self.X] = new_position

    def set_positionY(self, new_position: int, position_change=False) -> None:
        """
        Change la position ou la vitesse, mais seulement en Y.

        :param new_position: Nouvelle position ou vitesse
        :param position_change: Booléen, s'il est True change la vitesse
        :return: Change la position Y et la vitesse
        """
        if position_change:
            self.position_change[self.X] = new_position
        else:
            self.position[self.Y] = new_position

    def set_sprite(self, new_sprite):
        """
        Modifie la source de l'image.

        :param new_sprite: Nouvelle source image
        :return: Change la source de l'image.
        """
        self.sprite = new_sprite
