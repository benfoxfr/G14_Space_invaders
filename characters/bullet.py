import pygame


class Bullet:
    def __init__(self,position: list,position_change: list, state, img_path):
        """
        Initialisation des variables intiales du projet
        """
        self.position = position
        self.position_change = position_change
        self.state = state
        self.img_path = img_path

    def setter_position_change(self, new_position: list):
        self.position = new_position

    def get_position(self):
        """
        Accesseur de la position initiale du projectile
        """
        return self.position

    def get_position_change(self):
        """
        Accesseur de la position changée du projectile
        """
        return self.position_change

    def get_state(self):
        """
        Accesseur de l'état du projectile
        """
        return self.state

    def load_img(self):
        return pygame.image.load(self.img_path)



