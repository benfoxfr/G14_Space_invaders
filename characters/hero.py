from characters.character import Character
from characters.bullet import Bullet
from pygame import mixer
import pygame



class Hero(Character):

    def __init__(self, position: list[int], position_change: list[int], sprite: str):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(position, sprite, position_change)
        self.LASER_SOUND ='./wav/laser.wav'

    def move_limitations(self, limitation=736):
        """
        Permet à l'héro de rester dans le cadre du jeu s'il dépasse soit la valeur x ou y du cadre du jeu
        """

        self.position[self.X] += self.position_change[self.X]
        if self.position[self.X] <= 0:
            self.position[self.X] = 0
        elif self.position[self.X] >= limitation:
            self.position[self.X]= limitation


    def move(self, event, vitesse = 5):
        """
        Permet à l'héro de tirer dans le jeu
        :param event: l'action réalisée par le héro
        :param vitesse: la vitesse par défaut qui est 5
        """
        # La gestion des touches utilisateurs pour se déplacer
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.position_change[self.X] = - vitesse
            if event.key == pygame.K_RIGHT:
                self.position_change[self.X] = vitesse

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.position_change[self.X] = 0



    def shoot(self, screen, bullet: Bullet, event,):
        """
        Permet à l'utilisateur de se déplacer dans le jeu
        :param screen: l'écran du jeu
        :param bullet:  l'object bullet
        :param event: l'action réalisée par le joueur
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if bullet.state == "ready":
                bulletSound = mixer.Sound(self.LASER_SOUND)
                bulletSound.set_volume(0.4)
                bulletSound.play()
                # Get the current x cordinate of the spaceship
                bullet.state = "fire"
                bullet.position[self.X] = self.position[self.X]
                screen.blit(bullet.load_sprite, (bullet.get_position[self.X] + 16, bullet.get_position[self.Y] + 10))


