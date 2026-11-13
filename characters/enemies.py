from characters.character import Character

class Enemy(Character):
    def __init__(self, position: list[int], sprite: str, enemy_change: list[int], nombre_vies: int):
        super().__init__(position, sprite, enemy_change, nombre_vies)


    def game_over(self, screen, font):
        game_over = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over, (200, 250))

    def deplacement(self):
        pass





