from characters.character import Character

class Enemy(Character):
    def __init__(self, position: list[int], sprite: str, enemy_change: list[int], nombre_vies: int):
        super().__init__(position, sprite, enemy_change, nombre_vies)




