import pygame

from models.Ball import Ball
from models.Player import Player
from all_levels.L1 import L1
from all_levels.L2 import L2
from all_levels.L3 import L3
from all_levels.L4 import L4
from all_levels.L5 import L5
# from Start_page import Start_page

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
class MainProcess:

    def __init__(self, level):
        self.level = level

    def start(self):

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

        lives = 3
        score = 0
        record_score = ""

        rec = open('score.txt', 'r')
        for r in rec:
            record_score = r
        rec.close()


        if self.level == 1:
            itsLevel = L1(mobs, all_sprites, all_bricks)
        if self.level == 2:
            itsLevel = L2(mobs, all_sprites, all_bricks)
        if self.level == 3:
            itsLevel = L3(mobs, all_sprites, all_bricks)
        if self.level == 4:
            itsLevel = L4(mobs, all_sprites, all_bricks)
        if self.level == 5:
            itsLevel = L5(mobs, all_sprites, all_bricks)


        itsLevel.start()
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

                if bal.rect.y+10 > H - 13:
                    lives -= 1
                    pygame.time.wait(600)

                    start_game = False
                    bal.x = 380
                    bal.y = 460
                    player.rect.x = W // 2 - 25
                    bal.direction = 180
                    bal.bouncy(-180)
                    all_sprites.update()
                    all_sprites.draw(sc)

                    if lives == 0:
                        surf = pygame.image.load(r'images/gameover.jpg')
                        scale = pygame.transform.scale(surf, (800, 600))
                        rect = scale.get_rect(bottomleft=(0, 600))
                        sc.blit(scale, rect)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        game_end = False
                        # start_page = Start_page()
                        # TODO
                        return

                if pygame.sprite.collide_mask(player, bal):
                    diff = (player.rect.x + player.width / 2) - (bal.rect.x + bal.width / 2+10)
                    # bal.rect.y = H - player.rect.height - bal.rect.height-10
                    bal.bouncy(diff)

                break_collision = pygame.sprite.spritecollide(bal, all_bricks, False)

                for brick in break_collision:
                    if len(all_bricks) > 0:
                        bal.bouncy(0)
                    if pygame.sprite.collide_mask(bal, brick):
                        bal.bouncy(-90)
                    brick.kill()
                    score += 5

                    if len(all_bricks) == 0:
                        if int(record_score) < score:
                            wr = open('score.txt', 'w')
                            wr.write(str(score))

                        f2 = pygame.font.SysFont('arial', 60)
                        text = f2.render("Level Complete", 1, WHITE)
                        sc.blit(text, (200, 300))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        if self.level < 5:
                            m = MainProcess(self.level + 1)
                            m.start()
                        else:

                            game_end = False
                            return

            sc.fill(BLACK)
            all_sprites.draw(sc)

            if not start_game:
                f4 = pygame.font.SysFont('arial', 40)
                text4 = f4.render("Press space to start", 1, BLUE)
                sc.blit(text4, (230, 300))

            f3 = pygame.font.SysFont('arial', 32)
            text3 = f3.render("Lifes: " + str(lives), 1, BLUE)
            sc.blit(text3, (50, 10))
            f5 = pygame.font.SysFont('arial', 32)

            if int(record_score) < score:
                text5 = f5.render("New score: " + str(score), 1, BLUE)
                sc.blit(text5, (350, 10))
            else:
                text5 = f5.render("Score: " + str(score), 1, BLUE)
                sc.blit(text5, (450, 10))
            text6 = f5.render("Record: " + record_score, 1, BLUE)
            sc.blit(text6, (610, 10))

            pygame.display.flip()
            clock.tick(FPS)

