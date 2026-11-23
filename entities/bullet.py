import pygame
from pygame import mixer
from pygame.event import Event
from pygame.surface import SurfaceType

from entities.entity import Entity
import math

class Bullet(Entity):

    def __init__(self, position: list, sprite:str, position_change: list, state: str,):
        """
        Initialisation des variables intiales du projet
        """
        super().__init__(position,sprite,position_change)
        self.position_change = position_change
        self.state = state

    def get_state(self) -> str:
        """
        Accesseur de la variable d'instance state
        """

        return self.state

    def set_state(self, new_state: str) -> None:
        """
        Changer la variable d'instance state à new_state

        : param new_state: le nouvel état assigné à l'instance Bullet
        """

        self.state = new_state



    def shoot(self, screen: SurfaceType, pos_x : int,  event: Event, sound : str,score: int, other_bullet: str,bullet: str,pos_other_player: list[int], speed: int) -> None:
        """
        Tire des bullets lorsque le joueur appuye sur la touche ESPACE

        :param pos_other_player: La position d'un autre ennemi
        :param bullet: l'image originale de la bullet
        :param other_bullet: L'image d'un autre objet balle de la classe Bullet
        :param score: Le score acquis par le joueur
        :param speed: La vitesse de l'instance balle est 5 par défaut
        :param pos_x:  la position en X d'une instance Hero
        :param sound: le son lorsque le héro tire
        :param screen: l'écran du jeu pour afficher l'image de l'instance Bullet
        :param event:  une action réalisé par le joueur
        """

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.state == "ready":
                bulletSound = mixer.Sound(sound)
                bulletSound.set_volume(0.4)
                bulletSound.play()
                # Get the current x cordinate of the spaceship
                self.state = "fire"
                self.position[self.X] = pos_x
            if self.isCollision(pos_other_player) or self.position[self.Y] == 480:
                if score % 2 == 0  :
                    self.sprite = bullet
                    self.position_change[self.Y] = speed
                    screen.blit(self.load_sprite, (self.get_position[self.X] + 30, self.get_position[self.Y] + 40))

                elif score % 2 == 1:
                    self.sprite = other_bullet
                    self.position_change[self.Y] = speed * 2
                    screen.blit(self.load_sprite, (self.get_position[self.X] + 30, self.get_position[self.Y] - 40))








    def move(self, screen: SurfaceType) -> None:
        """
        Permet à l'instance bullet de se déplacer dans le jeu

        :param screen: l'objet écran qui va permettre d'affiche l'image de l'instance Bullet
        """

        if self.state == "fire":
            screen.blit(self.load_sprite, (self.get_position[self.X] + 30, self.get_position[self.Y] + 40))
            self.get_position[self.Y] -= self.get_position_change[self.Y]

    def move_limitations(self) -> None:
        """
        Remet l'état de la balle à ready lorsque l'ancienne balle est sortie du cadre du jeu
        """

        if self.get_position[self.Y] <= 0:
            self.get_position[self.Y] = 480
            self.state = 'ready'

    def isCollision(self, pos: list[int] , seuil_collision=27) -> bool:
        """
        Détermine si il y a une collision entre un autre joueur que le héro et un projectile (bullet dans ce cas-ci)

        :param seuil_collision: le seuil de la collision qui est mis à 27 par défaut
        :param pos: la position de l'autre joueur
        :return: True ssi la distance  euclidienne entre les coordonnées du projectile et ceux de  l'autre joueur est strictement inférieure  à 27
        """
        return math.sqrt(math.pow(pos[self.X] - self.position[self.X], 2) + (math.pow(pos[self.Y] - self.position[self.Y], 2))) < seuil_collision
