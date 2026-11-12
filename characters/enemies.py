from characters.character import Character

class Enemy(Character):
    def __init__(self, position: list[int], sprite: str, enemyX_change: int, enemyY_change: int, nombre_vies: int):
        super().__init__(position, sprite, enemyX_change, nombre_vies)
        self.enemy_change = [enemyX_change, enemyY_change]

    @property
    def get_position_change(self):
        return self.enemy_change

    def set_positionX_change(self, x):
        self.enemy_change[0] = x

    def set_positionY_change(self, y):
        self.enemy_change[1] = y




