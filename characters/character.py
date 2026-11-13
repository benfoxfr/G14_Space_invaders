import pygame


class Character:
    def __init__(self, position: list[int], sprite: str, position_change: list[int], nombre_vies: int):
        """
        Initialisation des variables
        """
        if len(position) != 2:
            raise ValueError(f"La liste {position} doit contenir la position [x, y]")
        self.position = position
        self.sprite = sprite
        if len(position_change) != 2:
            raise ValueError(f"La liste {position_change} doit contenir la position [x, y]")
        self.position_change = position_change
        self.nombre_vies = nombre_vies

    @property
    def get_sprite(self):
        """
        Accesseur du chemin source image du charactère
        """
        return self.sprite

    @property
    def get_position(self):
        """
        Accesseur de la position
        """
        return self.position

    @property
    def get_position_change(self):
        """
        Accesseur de l'abcisse de la position du charactère
        """
        return self.position_change

    @property
    def load_sprite(self):
        """
        Chargement du chemin source de l'image de charactère

        """
        return pygame.image.load(self.sprite)

    def set_positionX(self, new_position, position_change=False):
        """
        Initialisation de la position x du charactère
        """
        if position_change:
            self.position_change[0] = new_position
        else:
            self.position[0] = new_position

    def set_positionY(self, new_position, position_change=False):
        """
        Initialisation de la position y du charactère
        """
        if position_change:
            self.position_change[0] = new_position
        else:
            self.position[1] = new_position

    def set_sprite(self, new_sprite):
        """
        Initialisation du chemin fichier de l'image de charactère
        """
        self.sprite = new_sprite

    def get_nombres_vies(self):
        """
        Accesseur du nombre de vies d'un caractère
        """
        return self.nombre_vies

