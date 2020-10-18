import pygame
from Level import Level
from MainProcess import MainProcess

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (120, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FPS = 60

class Levels:
    k = 5

    def __init__(self, sc, w, h):
        self.sc = sc
        self.w = w
        self.h = h

    def update(self):
        self.sc.fill(BLACK)
        levels = []

        l1 = Level(self.sc, self.w, self.h, 0, 0, 0)
        levels.append(l1)
        l2 = Level(self.sc, self.w, self.h, 1, 0, 1)
        levels.append(l2)
        l3 = Level(self.sc, self.w, self.h, 2, 0, 2)
        levels.append(l3)
        l4 = Level(self.sc, self.w, self.h, 0, 1, 3)
        levels.append(l4)
        l5 = Level(self.sc, self.w, self.h, 1, 1, 4)
        levels.append(l5)

        surf = pygame.image.load(r'images/levels/back.png')
        scale = pygame.transform.scale(surf, (self.w // 7, self.h // 6))
        rect = scale.get_rect(bottomleft=(self.w // 5 * 4, self.h // 13 * 12))
        self.sc.blit(scale, rect)
        pygame.display.update()
        flag = True
        pr_motion = -1
        while flag:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (pos[0] >= self.w // 5 * 4 and pos[0] <= self.w // 5 *  + self.w // 7 and pos[1] <= self.h // 13 * 12
                            and pos[1] >= self.h // 13 * 12 - self.h // 6):
                        flag = False
                    for i in range(0, 5):
                        x = pos[0] - levels[i].c_W
                        y = pos[1] - levels[i].c_H
                        if (x * x) + (y * y) <= levels[i].r * levels[i].r // 10 * 3:
                            if pygame.MOUSEBUTTONDOWN:
                                level = i + 1
                                breakOut = MainProcess(level)
                                breakOut.start()


            pos = pygame.mouse.get_pos()
            motion = -1

            for i in range(0, 5):

                x = pos[0] - levels[i].c_W
                y = pos[1] - levels[i].c_H
                if (x * x) + (y * y) <= levels[i].r * levels[i].r // 10 * 3:
                    motion = i




            if motion != -1 and motion != pr_motion and pr_motion != -1:
                levels[motion].bigger()
                levels[pr_motion].smaller()
                pr_motion = motion
                pygame.display.update()


            if motion == -1 and pr_motion !=-1:
                levels[pr_motion].smaller()
                pr_motion = motion
                pygame.display.update()

            if motion != -1 and motion != pr_motion and pr_motion == -1:
                levels[motion].bigger()
                pr_motion = motion
                pygame.display.update()



