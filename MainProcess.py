import pygame

from models.Ball import Ball
from models.Player import Player
from all_levels.L1 import L1
from all_levels.L2 import L2
from all_levels.L3 import L3
from all_levels.L4 import L4
from all_levels.L5 import L5

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
        self.score = 0

    def start(self):

        sc = pygame.display.set_mode((W, H))
        surf = pygame.image.load(r'images/sky.jpg')
        surf_bg = pygame.transform.scale(surf, (W, H))
        surf_rect = surf_bg.get_rect(center=(W // 2, H // 2))
        clock = pygame.time.Clock()
        heart_img = pygame.image.load(r'images/heart.png')
        heart_trans = pygame.transform.scale(heart_img, (30, 30))


        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        ball = pygame.sprite.Group()

        player = Player()
        bal = Ball(RED)
        bal.rect.x = 400
        bal.rect.y = 460
        bal.bouncy(-180)

        all_sprites.add(player)
        all_sprites.add(bal)
        all_bricks = pygame.sprite.Group()
        bricks_group = pygame.sprite.Group()

        lives = 5
        # score = 0
        record_score = ""

        pygame.mixer.music.load(r'music/fon2.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        sound_udar = pygame.mixer.Sound(r'music/udar.wav')
        sound_gameover = pygame.mixer.Sound(r'music/gameover.wav')
        sound_button = pygame.mixer.Sound(r'music/gameover.wav')

        rec = open('score.txt', 'r')
        for r in rec:
            record_score = r
        rec.close()

        if self.level == 1:
            itsLevel = L1(mobs, all_sprites, all_bricks, bricks_group)
        if self.level == 2:
            itsLevel = L2(mobs, all_sprites, all_bricks, bricks_group)
        if self.level == 3:
            itsLevel = L3(mobs, all_sprites, all_bricks, bricks_group)
        if self.level == 4:
            itsLevel = L4(mobs, all_sprites, all_bricks, bricks_group)
        if self.level == 5:
            itsLevel = L5(mobs, all_sprites, all_bricks, bricks_group)

        itsLevel.start()
        game_end = True
        start_game = False
        pause_flag = False
        while game_end:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_end = False
                    exit()
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN and pos[0] > 5 and pos[0] < 40 and pos[1] > 10 and pos[1] < 45:
                    sound_button.play()
                    if pause_flag:
                        pause_flag = False
                    else:
                        pause_flag = True

            if pause_flag:
                continue


            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE]:
                start_game = True

            if start_game:
                all_sprites.update()

                if bal.rect.y > H - player.height - 5:
                    lives -= 1
                    pygame.time.wait(600)

                    start_game = False
                    bal.x = 400
                    bal.y = 460
                    player.x = 380
                    player.y = 460
                    player.rect.x = W // 2 - 25
                    bal.direction = 180
                    bal.bouncy(-180)
                    all_sprites.update()
                    all_sprites.draw(sc)

                    if lives == 0:
                        surf = pygame.image.load(r'images/gameover.jpg')
                        pygame.mixer.music.pause()
                        sound_gameover.play()
                        pygame.mixer.music.unpause()
                        scale = pygame.transform.scale(surf, (800, 600))
                        rect = scale.get_rect(bottomleft=(0, 600))
                        sc.blit(scale, rect)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        game_end = False
                        m = MainProcess(self.level)
                        m.start()
                        break

                if pygame.sprite.collide_rect(player, bal):
                    print(bal.rect.bottom)
                    print(player.rect.bottom)
                    if bal.rect.bottom >= player.rect.bottom - bal.radius and player.rect.right >= bal.rect.left and \
                            bal.rect.right >= player.rect.left:
                        diff = (player.rect.x + player.width / 2) - (bal.rect.x + bal.width / 2)

                        bal.rect.y = H - player.rect.height - bal.rect.height - 15
                        bal.bouncy(diff)

                break_collision = pygame.sprite.spritecollide(bal, all_bricks, False)

                if break_collision:
                    sound_udar.play()
                    hit_rect = break_collision[0].rect
                    if hit_rect.left > bal.rect.left or bal.rect.right > hit_rect.right:
                        bal.vertical(0)

                    if hit_rect.bottom < bal.rect.bottom or hit_rect.bottom > bal.rect.bottom:
                        print(2)
                        print(3)
                        bal.bouncy(0)
                    self.score += 5

                    hits = pygame.sprite.spritecollide(bal, bricks_group, True)

                    if pygame.key.get_pressed()[pygame.K_0]:
                        for sp in all_bricks:
                            sp.kill()


                    if len(all_bricks) == 0 :
                        if int(record_score) < self.score:
                            wr = open('score.txt', 'w')
                            wr.write(str(self.score))

                        surf = pygame.image.load(r'images/levelCompleted.png')
                        scale = pygame.transform.scale(surf, (400, 300))
                        rect = scale.get_rect(bottomleft=(200, 450))
                        sc.blit(scale, rect)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        if self.level < 5:
                            m = MainProcess(self.level + 1)
                            m.start()
                        else:
                            game_end = False
                        break

                # for brick in break_collision:
                #     if len(all_bricks) > 0:
                #         bal.bouncy(-90)
                #     if pygame.sprite.collide_rect(bal, brick):
                #         bal.bouncy(0)
                #     brick.kill()
                #     score += 5
                #
                #     if len(all_bricks) == 0:
                #         if int(record_score) < score:
                #             wr = open('score.txt', 'w')
                #             wr.write(str(score))
                #
                #         f2 = pygame.font.SysFont('arial', 60)
                #         text = f2.render("Level Complete", 1, WHITE)
                #         sc.blit(text, (200, 300))
                #         pygame.display.flip()
                #         pygame.time.wait(1000)
                #         if self.level < 5:
                #             m = MainProcess(self.level + 1)
                #             m.start()
                #         else:
                #
                #             game_end = False
                #             return

            sc.fill(BLACK)
            sc.blit(surf_bg, surf_rect)
            pygame.draw.rect(sc, GREEN, (10, 15, 10, 30))
            pygame.draw.rect(sc, GREEN, (25, 15, 10, 30))
            all_sprites.draw(sc)

            if not start_game:
                f4 = pygame.font.SysFont('arial', 40)
                text4 = f4.render("Press space to start", 1, YELLOW)
                sc.blit(text4, (230, 300))

                bal.start()
                player.start()

                key = pygame.key.get_pressed()

                if key[pygame.K_RIGHT] or key[pygame.K_d]:
                    if bal.rect.right > W - 50 and player.rect.right > W - 10:
                        bal.rect.right = W - 50
                        player.rect.right = W - 10
                    else:
                        bal.x += 10
                        player.x += 10
                if key[pygame.K_LEFT] or key[pygame.K_a]:
                    if bal.rect.left < 50 and player.rect.left < 10:
                        bal.rect.left = 0
                        player.rect.left = 0
                    else:
                        bal.x -= 10
                        player.x -= 10

            for i in range(0, lives):
                sc.blit(heart_trans, (65 + i * 45, 15))

            f = pygame.font.SysFont('arial', 32)
            if int(record_score) < self.score:
                text5 = f.render("New score: " + str(self.score), 1, GREEN)
                sc.blit(text5, (350, 10))
            else:
                text5 = f.render("Score: " + str(self.score), 1, GREEN)
                sc.blit(text5, (450, 10))
            text6 = f.render("Record: " + record_score, 1, GREEN)
            sc.blit(text6, (610, 10))

            pygame.display.flip()
            pygame.display.update()
            clock.tick(FPS)
