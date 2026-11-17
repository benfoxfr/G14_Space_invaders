from characters.character import Character

class Enemy(Character):
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





