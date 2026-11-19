from characters.entity import Entity
import math

class Bullet(Entity):

    def __init__(self, position: list, sprite:str, position_change: list, state: str,):
        """
        Initialisation des variables intiales du projet
        """
        super().__init__(position,sprite,position_change)
        self.position_change = position_change
        self.state = state

    def get_state(self):
        """
        Accesseur de la valeur de l'état
        """
        return self.state

    def set_state(self, new_state: str):
        """
        Mettre la valeur de l'état à un nouvel état
        """
        self.state = new_state

    def fire(self, screen):
        """
        Cette fonction permet de tirer une balle du vaisseau
        """

        if self.state == "fire":
            screen.blit(self.load_sprite, (self.get_position[self.X] + 16, self.get_position[self.Y] + 10))
            self.get_position[self.Y] -= self.get_position_change[self.Y]

    def move_limitations(self):
        """
        Cette fonction permet que les balles du vaisseau reste dans le cadre du jeu
        """
        if self.get_position[self.Y] <= 0:
            self.get_position[self.Y] = 480
            self.state = 'ready'

    def isCollision(self, pos: list[int] , seuil_collision=27) -> bool:
        """
        Détermine si il y a une collision entre un autre joueur que le héro et un projectile (bullet dans ce cas-ci)
        :param seuil_collision: le seuil de la collision qui est mis à 27 par défaut
        :param pos: la position de l'autre joueur
        :return: True ssi la distance entre la distance euclidienne entre le projectile et l'autre joueur est strictement inférieure  à 27
        """
        return math.sqrt(math.pow(pos[self.X] - self.position[self.X], 2) + (math.pow(pos[self.Y] - self.position[self.Y], 2))) < seuil_collision
