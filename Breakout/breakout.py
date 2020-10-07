import pygame

from gerasimov_itis_python2k_11900.project.Breakout.Ball import Ball
from gerasimov_itis_python2k_11900.project.Breakout.Mobs import Mobs
from gerasimov_itis_python2k_11900.project.Breakout.Player import Player

pygame.init()
pygame.mixer.init()

W = 800
H = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
ball = pygame.sprite.Group()

player = Player()
bal = Ball(RED)
bal.rect.x = 380
bal.rect.y = 460
bal.bouncy(-180)

all_sprites.add(player)
all_sprites.add(bal)
all_bricks = pygame.sprite.Group()

lives = 5

for i in range(7):
    m = Mobs(YELLOW, 80, 30)
    m.rect.x = 60 + i * 100
    m.rect.y = 60
    mobs.add(m)
    all_sprites.add(m)
    all_bricks.add(m)
for i in range(7):
    m = Mobs(RED, 80, 30)
    m.rect.x = 60 + i * 100
    m.rect.y = 100
    mobs.add(m)
    all_sprites.add(m)
    all_bricks.add(m)
for i in range(7):
    m = Mobs(GREEN, 80, 30)
    m.rect.x = 60 + i * 100
    m.rect.y = 140
    mobs.add(m)
    all_sprites.add(m)
    all_bricks.add(m)

game_end = True
start_game = False
while game_end:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_end = False
            exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        start_game = True

    if start_game:
        all_sprites.update()

        if bal.rect.y > H - 10:
            lives -= 1

            start_game = False
            bal.x = 380
            bal.y = 460
            player.rect.x = W // 2 - 25
            bal.direction = 200
            bal.bouncy(-180)
            all_sprites.update()
            all_sprites.draw(sc)

            if lives == 0:
                f1 = pygame.font.SysFont('arial', 70)
                text = f1.render("GAME OVER", 1, RED)
                sc.fill(BLACK)
                sc.blit(text, (250, 300))
                pygame.display.flip()
                pygame.time.wait(1000)
                game_end = False
                exit()

        if pygame.sprite.collide_mask(player, bal):
            diff = (player.rect.x + player.width / 2) - (bal.rect.x + bal.width / 2)

            bal.rect.y = H - player.rect.height - bal.rect.height - 2

            bal.bouncy(diff)

        break_collision = pygame.sprite.spritecollide(bal, all_bricks, False)

        for brick in break_collision:
            if len(all_bricks) > 0:
                bal.bouncy(0)
            if pygame.sprite.collide_mask(bal, brick):
                bal.bouncy(-90)
            brick.kill()

            if len(all_bricks) == 0:
                f2 = pygame.font.SysFont('arial', 60)
                text = f2.render("Level Complete", 1, WHITE)
                sc.blit(text, (200, 300))
                pygame.display.flip()
                pygame.time.wait(1000)

                game_end = False
                exit()

    sc.fill(BLACK)
    all_sprites.draw(sc)

    if not start_game:
        f4 = pygame.font.SysFont('arial', 40)
        text4 = f4.render("Press space to start", 1, BLUE)
        sc.blit(text4, (250, 300))

    f3 = pygame.font.SysFont('arial', 32)
    text3 = f3.render("Lifes" + str(lives), 1, BLUE)
    sc.blit(text3, (50, 10))

    pygame.display.flip()
    clock.tick(FPS)
