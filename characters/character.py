import pygame


class Character:
    def __init__(self, positionX: int, positionY: int, sprite: str, characterX_change: int):
        self.position = [positionX, positionY]
        self.sprite = sprite
        self.characterX_change = characterX_change

    @property
    def get_sprite(self):
        return self.sprite

    @property
    def get_position(self):
        return self.position

    @property
    def get_characterX_change(self):
        return self.characterX_change

    @property
    def get_sprite(self):
        return self.sprite

    @property
    def load_sprite(self):
        return pygame.image.load(self.sprite)

    def set_positionX(self, new_position):
        self.position[0] = new_position

    def set_positionY(self, new_position):
        self.position[1] = new_position

    def set_characterX_change(self, new_character_change):
        self.characterX_change = new_character_change

    def set_sprite(self, new_sprite):
        self.sprite = new_sprite

    def move(self):
        pass

    def fire(self):
        pass

