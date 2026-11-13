import math
import random
import pygame
from pygame import mixer
from characters.hero import Hero
from characters.enemies import Enemy
from characters.bullet import Bullet
from os import chdir

X = 0
Y = 1
TEXTX = 10
TEXTY = 10
GAME_OVER = "GAME OVER"
CONTINUE = "Continer le jeu !"
COLLISION_LIMITE = 27
CARRE = 2
EXPLOSION_SOUND = "./wav/explosion.wav"
BACKGROUND = "./img/background.png"
BACKGROUND_SOUND = "./wav/background.wav"
ICON = './img/ufo.png'
PLAYER = './img/player.png'
ENEMY = './img/enemy.png'
BULLET = './img/bullet.png'
LASER_SOUND = './wav/laser.wav'
READY = "ready"
FIRE = "fire"



def isCollision(enemyX: int, enemyY: int, bulletX: int, bulletY: int) -> bool:
    """
    Si la distance euclidienne entre les coordonées de l'enemy et ceux du boulet est strictement inférieur à 27
    :param enemyX: la postion x de l'enemy
    :param enemyY: la position y de l'enemy
    :param bulletX: le position x du projectile
    :param bulletY: la position y du projectile
    :return:
    """
    return math.sqrt(math.pow(enemyX - bulletX, CARRE) + (math.pow(enemyY - bulletY, CARRE))) < COLLISION_LIMITE

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
    hero = Hero([370, 480], PLAYER, [0, 0], 0)

    # Enemy
    num_of_enemies = random.randint(25, 30)
    enemies = [Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY, [1, 40], 0) for _ in range(num_of_enemies)]

    # Bullet

    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving

    bullet = Bullet([hero.position[0], 480],[0,11],BULLET,READY)


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

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.set_positionX(-5, position_change=True)
                if event.key == pygame.K_RIGHT:
                    hero.set_positionX(5, position_change=True)
                if event.key == pygame.K_SPACE:
                    if bullet.state == READY:
                        bulletSound = mixer.Sound(LASER_SOUND)
                        bulletSound.set_volume(0.4)
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bullet.get_position[X] = hero.get_position[X]
                        bullet.state = FIRE
                        screen.blit(bullet.load_sprite, (bullet.get_position[X] + 16, bullet.get_position[Y] + 10))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    hero.set_positionX(0, position_change=True)

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        hero.get_position[X] += hero.get_position_change[X]
        if hero.get_position[X] <= 0:
            hero.set_positionX(0)
        elif hero.get_position[X] >= 736:
            hero.set_positionX(736)

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemies[i].get_position[Y] > 440:
                for j in range(num_of_enemies):
                    enemies[j].set_positionX(2000)

                over_text = over_font.render(GAME_OVER, True, (255, 255, 255))
                screen.blit(over_text, (200, 250))
                break

            enemies[i].get_position[X] += enemies[i].get_position_change[X]
            if enemies[i].get_position[X] <= 0:
                enemies[i].set_positionX(1, position_change=True)
                enemies[i].get_position[Y] += enemies[i].get_position_change[Y]
            elif enemies[i].get_position[X] >= 736:
                enemies[i].set_positionX(-1, position_change=True)
                enemies[i].get_position[Y] += enemies[i].get_position_change[Y]

            # Collision
            collision = isCollision(enemies[i].get_position[X], enemies[i].get_position[Y], bullet.get_position[X], bullet.get_position[Y])
            if collision:
                explosionSound = mixer.Sound(EXPLOSION_SOUND)
                explosionSound.set_volume(0.2)
                explosionSound.play()
                bullet.get_position[Y] = 480
                bullet.set_state(READY)
                score_value += 1
                enemies[i].get_position[X] = random.randint(0, 736)
                enemies[i].get_position[Y] = random.randint(50, 150)

            screen.blit(enemies[i].load_sprite, enemies[i].get_position)

        # Bullet Movement
        if bullet.get_position[Y] <= 0:
            bullet.get_position[Y] = 480
            bullet.set_state(READY)

        if bullet.state == FIRE:
            screen.blit(bullet.load_sprite, (bullet.get_position[X] + 16, bullet.get_position[Y] + 10))
            bullet.get_position[Y] -= bullet.get_position_change()[Y]

        screen.blit(hero.load_sprite, hero.get_position)

        # Score
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (TEXTX, TEXTY))
        pygame.display.update()


if __name__ == "__main__":
    main()