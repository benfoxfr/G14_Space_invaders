import pygame


class Character:
    def __init__(self, position: list[int], sprite: str, characterX_change: int, nombre_vies: int):
        """
        Initialisation des variables
        """
        self.position = position
        self.sprite = sprite
        self.characterX_change = characterX_change
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
    def get_characterX_change(self):
        """
        Accesseur de l'abcisse de la position du charactère
        """
        return self.characterX_change

    @property
    def load_sprite(self):
        """
        Chargement du chemin source de l'image de charactère

        """
        return pygame.image.load(self.sprite)

    def set_positionX(self, new_position):
        """
        Initialisation de la position x du charactère
        """
        self.position[0] = new_position

    def set_positionY(self, new_position):
        """
        Initialisation de la position y du charactère
        """
        self.position[1] = new_position

    def set_characterX_change(self, new_character_change):
        """
        Changement de la position x du charactère
        """
        self.characterX_change = new_character_change

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

    def move(self):
        pass

    def fire(self):
        pass

