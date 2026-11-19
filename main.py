import random
import pygame
from pygame import mixer
from characters.hero import Hero
from characters.enemies import Enemy
from characters.bullet import Bullet

X = 0
Y = 1
TEXTX = 10
TEXTY = 10
VITESSE_ENEMY = 2
NUM_OF_ENEMIES = 20
EXPLOSION_SOUND = "./wav/explosion.wav"
BACKGROUND = "./img/background.png"
BACKGROUND_SOUND = "./wav/background.wav"
ICON = './img/ufo.png'
PLAYER = './img/player.png'
ENEMY = './img/enemy.png'
BULLET = './img/bullet.png'
LASER_SOUND = './wav/laser.wav'


def main():
    # Intialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load(BACKGROUND)

    # Sound
    mixer.music.load(BACKGROUND_SOUND)
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Space Invader")
    icon = pygame.image.load(ICON)
    pygame.display.set_icon(icon)

    # Player
    hero = Hero([370, 480],  [0, 0], PLAYER)

    # Enemy
    enemies = [Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY, [VITESSE_ENEMY, 40]) for _ in range(NUM_OF_ENEMIES)]

    # Bullet

    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving

    bullet = Bullet([hero.position[0], 480], BULLET, [0, 10], "ready")

    # Score

    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    # Game Loop
    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            hero.shoot(screen, bullet, event, LASER_SOUND)
            hero.move(event)

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        # Permet à l'héro de rester dans le cadre du jeu
        hero.move_limitations()

        # Enemy Movement
        for i in range(NUM_OF_ENEMIES):

            # Game Over
            if enemies[i].get_position[Y] > 440:
                for j in range(NUM_OF_ENEMIES):
                    enemies[j].set_positionX(2000)

                enemies[i].game_over(screen, over_font)

            enemies[i].deplacement(VITESSE_ENEMY)

            # Collision
            collision = bullet.isCollision(enemies[i].position)
            if collision:
                enemies[i].mort(EXPLOSION_SOUND, bullet)
                score_value += 1

            screen.blit(enemies[i].load_sprite, enemies[i].get_position)

        # Bullet Movement
        bullet.move_limitations()

        # Pemettre de tirer des balles du vaisseau spatiale
        bullet.fire(screen)

        screen.blit(hero.load_sprite, hero.get_position)

        # Score
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (TEXTX, TEXTY))
        pygame.display.update()


if __name__ == "__main__":
    main()
