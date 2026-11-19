import random
import pygame
from pygame import mixer
from entities.hero import Hero
from entities.enemies import Enemy
from entities.bullet import Bullet

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

    # Initialisation du joueur et des ennemis, ainsi que les tirs
    hero = Hero([370, 480],  [0, 0], PLAYER)
    enemies = [Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY, [VITESSE_ENEMY, 40]) for _ in range(NUM_OF_ENEMIES)]
    bullet = Bullet([hero.position[0], 480], BULLET, [0, 10], "ready")

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over = over_font.render("GAME OVER", True, (255, 255, 255))

    # Boucle de gameplay
    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 255, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            bullet.shoot(screen,hero.position[X], event, LASER_SOUND)
            hero.move(event)

        # Permet au héro de rester dans le cadre du jeu
        hero.move_limits()

        # Boucle déplacement des ennemis
        for i in range(NUM_OF_ENEMIES):

            # Game Over
            if enemies[i].get_position[Y] > 440:
                for j in range(NUM_OF_ENEMIES):
                    enemies[j].set_positionX(2000)

                screen.blit(game_over, (200, 250))

            enemies[i].move(VITESSE_ENEMY)

            # Collision
            collision = bullet.isCollision(enemies[i].position)
            if collision:
                enemies[i].death(EXPLOSION_SOUND, bullet)
                score_value += 1

            screen.blit(enemies[i].load_sprite, enemies[i].get_position)

        # Bullet Movement
        bullet.move_limitations()

        # Permet de déplacer la balle dans le jeu
        bullet.move(screen)

        screen.blit(hero.load_sprite, hero.get_position)

        # Score
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (TEXTX, TEXTY))
        pygame.display.update()


if __name__ == "__main__":
    main()
