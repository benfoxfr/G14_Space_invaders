from pygame.font import FontType
from pygame.surface import SurfaceType
from entities.entity import Entity
from entities.bullet import Bullet
from pygame import mixer
import random


class Enemy(Entity):

    def __init__(self, position: list[int], sprite: str, position_change: list[int]) -> None:
        super().__init__(position, sprite, position_change)

    def game_over(self, screen: SurfaceType, font: FontType):
        '''
        Affiche le message game over dans la surface de jeu

        :param screen: La surface de jeu
        :param font: Police de texte
        :return: Affiche le Game Over
        '''
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (200, 250))

    def move(self, speed: int, position_max=736) -> None:
        '''
        Cette méthode s'occupe du déplacement des ennemis, position_max est adapté pour la largeur (X) de 800.
        À modifier si la zone de jeu est plus large.

        :param speed: Entier qui s'occupe de la vitesse de déplacement
        :param position_max: Distance max en de X
        :return: Change la position des ennemis
        '''
        self.position[self.X] += self.position_change[self.X]
        if self.position[self.X] <= 0:
            self.position_change[self.X] = speed
            self.position[self.Y] += self.position_change[self.Y]
        elif self.position[self.X] >= position_max:
            self.position_change[self.X] = -speed
            self.position[self.Y] += self.position_change[self.Y]

    def death(self, sound: str, bullet: Bullet, position_init=480, volume=0.2) -> None:
        '''
        Mort d'un ennemi touché par une balle

        :param sound: Son de mort d'un ennemi
        :param bullet: La balle qu'il l'a touchée
        :param position_init: Position Y de la balle à réinitialiser
        :param volume: Volume du son
        :return: Active le son de mort d'un ennemi et change sa position aléatoirement.
        '''
        explosionSound = mixer.Sound(sound)
        explosionSound.set_volume(volume)
        explosionSound.play()
        bullet.set_positionY(position_init)
        bullet.set_state("ready")
        self.position[self.X] = random.randint(0, 736)
        self.position[self.Y] = random.randint(50, 150)





