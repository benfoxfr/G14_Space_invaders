from characters.entity import Entity
from characters.bullet import Bullet
from pygame import mixer
import random


class Enemy(Entity):
    def __init__(self, position: list[int], sprite: str, position_change: list[int]):
        super().__init__(position, sprite, position_change)

    def game_over(self, screen, font):
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (200, 250))

    def deplacement(self, vitesse, taille_ecran=736):
        self.position[self.X] += self.position_change[self.X]
        if self.position[self.X] <= 0:
            self.position_change[self.X] = vitesse
            self.position[self.Y] += self.position_change[self.Y]
        elif self.position[self.X] >= taille_ecran:
            self.position_change[self.X] = -vitesse
            self.position[self.Y] += self.position_change[self.Y]

    def mort(self, son: str, bullet: Bullet, position_tir=480, volume=0.2):
        explosionSound = mixer.Sound(son)
        explosionSound.set_volume(volume)
        explosionSound.play()
        bullet.set_positionY(position_tir)
        bullet.set_state("ready")
        self.position[self.X] = random.randint(0, 736)
        self.position[self.Y] = random.randint(50, 150)





