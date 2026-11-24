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
VITESSE_BULLET = 10
VITESSE_ENEMY_MAX = 5
NUM_OF_ENEMIES = 5  # Celui-ci est multiplié par 3, 5 lents, 5 moyens, 5 rapides
EXPLOSION_SOUND = "./wav/explosion.wav"
BACKGROUND = "./img/background.png"
BACKGROUND_SOUND = "./wav/background.wav"
ICON = './img/ufo.png'
PLAYER = './img/player.png'
ENEMY_SLOW = './img/enemy_slow.png'
ENEMY = './img/enemy.png'
ENEMY_FAST = './img/enemy_fast.png'
BULLET = './img/bullet.png'
FAST_BULLET = './img/fast_bullet.jpg'
LASER_SOUND = './wav/laser.wav'


def main():
    # Intialize the pygame
    pygame.init()

    bullet = 0

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

    enemies = []
    for vitesse in range(1, VITESSE_ENEMY_MAX+1):
        for _ in range(NUM_OF_ENEMIES):
            if vitesse == 1:
                enemies.append(Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY_SLOW, [vitesse, 40]))
            elif vitesse == VITESSE_ENEMY_MAX//2+1:
                enemies.append(Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY, [vitesse, 40]))
            elif vitesse == VITESSE_ENEMY_MAX:
                enemies.append(Enemy([random.randint(0, 736), random.randint(50, 150)], ENEMY_FAST, [vitesse, 40]))

    bullets = (Bullet([hero.get_position[X], 480], BULLET, [0, VITESSE_BULLET], "ready"),
               Bullet([hero.get_position[X], 480], FAST_BULLET, [0, VITESSE_BULLET*2], "ready"))

    # Score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    game_over = over_font.render("GAME OVER", True, (255, 255, 255))
    is_GameOver = False

    # Boucle de gameplay
    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 255, 0))
        # Background Image
        screen.blit(background, (0, 0))
        for i, event in enumerate(pygame.event.get()):
            if event.type == pygame.QUIT:
                running = False
            if not is_GameOver:
                bullets[bullet].shoot(screen, hero.position[X], enemies[i].position, event, LASER_SOUND)

            hero.move(event)

        # Permet au héro de rester dans le cadre du jeu
        hero.move_limits()

        # Boucle déplacement des ennemis
        for i in range(len(enemies)):

            # Game Over
            if enemies[i].get_position[Y] > 440:
                for j in range(len(enemies)):
                    enemies[j].set_positionX(2000)
                    hero.set_positionY(1000)
                screen.blit(game_over, (200, 250))
                is_GameOver = True

            if enemies[i].get_position_change[X] == 1:
                enemies[i].move(1)
            elif enemies[i].get_position_change[X] == VITESSE_ENEMY_MAX//2+1:
                enemies[i].move(VITESSE_ENEMY_MAX//2+1)
            elif enemies[i].get_position_change[X] == VITESSE_ENEMY_MAX:
                enemies[i].move(VITESSE_ENEMY_MAX)
            else:
                enemies[i].move(abs(enemies[i].get_position_change[X]))

            # Collision
            collision = bullets[bullet].isCollision(enemies[i].position)
            if collision:
                enemies[i].death(EXPLOSION_SOUND, bullets[bullet])
                score_value += 1
                if score_value % 2 == 0:
                    bullet = 1
                else:
                    bullet = 0

            screen.blit(enemies[i].load_sprite, enemies[i].get_position)

        # Bullet Movement
        bullets[bullet].move_limitations()

        # Permet de déplacer la balle dans le jeu
        bullets[bullet].move(screen)

        screen.blit(hero.load_sprite, hero.get_position)

        # Score
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (TEXTX, TEXTY))
        pygame.display.update()


if __name__ == "__main__":
    main()
