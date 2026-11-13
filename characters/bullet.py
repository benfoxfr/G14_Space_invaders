import pygame
from characters.character import Character



class Bullet(Character):
    X = 0
    Y = 1

    FIRE = "fire"
    READY = "ready"
    def __init__(self, position: list,position_change: list, sprite:str, state: str, x_change= None,):
        """
        Initialisation des variables intiales du projet
        """
        super().__init__(position,sprite,x_change,0)
        self.position_change = position_change
        self.state = state


    def get_position_change(self):
        return self.position_change
    def get_state(self):
        """
        Accesseur de la valeur de l'état
        """
        return self.state
    def set_state(self, new_state):
        """
        Mettre la valeur de l'état à un nouvel état
        """
        self.state = new_state

    def move(self, screen):
        print(list(self.get_position))
        if self.get_position[self.Y] <= 0:
            self.get_position[self.Y] = 480
            self.set_state(self.READY)

        if self.get_state == self.FIRE:
            screen.blit(self.load_sprite, (self.get_position[self.X] + 16, self.get_position[self.Y] + 10))
            self.get_position[self.Y] -= self.get_position_change[self.Y]





