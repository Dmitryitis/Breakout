import pygame

from gerasimov_itis_python2k_11900.project.Breakpoint.Ball import Ball
from gerasimov_itis_python2k_11900.project.Breakpoint.Mobs import Mobs
from gerasimov_itis_python2k_11900.project.Breakpoint.Player import Player

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
bal.rect.x = 490
bal.rect.y = 500

all_sprites.add(player)
all_sprites.add(bal)
all_bricks = pygame.sprite.Group()

lives = 3

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
while game_end:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_end = False
            exit()

    all_sprites.update()

    if bal.rect.y > H - 9:
        lives -= 1
        bal.rect.x = 300
        bal.rect.y = 300
        if lives == 0:
            f1 = pygame.font.SysFont('arial', 70)
            text = f1.render("GAME OVER", 1, RED)
            sc.fill(BLACK)
            sc.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(1000)
            game_end = False
            exit()

    if pygame.sprite.collide_mask(player,bal):
        diff = (player.rect.x + player.width / 2) - (bal.rect.x + bal.width / 2)

        bal.rect.y = H - player.rect.height - bal.rect.height-1

        bal.bouncy(diff)

    break_collision = pygame.sprite.spritecollide(bal, all_bricks, False)
    for brick in break_collision:
        brick.kill()
        if len(all_bricks) > 0:
            bal.bouncy(0)
        if len(all_bricks) == 0:
            f2 = pygame.font.SysFont('arial', 60)
            text = f2.render("Level Complete", 1, WHITE)
            sc.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            game_end = False
            exit()

    sc.fill(BLACK)
    all_sprites.draw(sc)

    pygame.display.flip()
    clock.tick(FPS)
