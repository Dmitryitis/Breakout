import pygame

RED = (120, 0, 0)

class Level:


    def __init__(self, sc, w, h, w_num, h_num, num):

        self.sc = sc

        self.w = (w - w // 5) // 3
        self.h = (h - h // 5) // 2

        if h_num == 1:
            self.otstW = self.w * 3 // 2 + w // 10
            if w_num == 0:
                self.otstW -= self.w
        else:
            self.otstW = w_num * self.w + w // 10

        self.otstH = h_num * self.h + h // 10
        self.n_surf = pygame.image.load(r'images/levels/' + str(num + 1) + '.png')
        if self.w > self.h:
            self.r = self.h // 2
        else:
            self.r = self.w // 2

        self.n_scale = pygame.transform.scale(self.n_surf, (self.r, self.r))
        self.n_rect = self.n_scale.get_rect(bottomleft=(self.otstW + self.w // 2 - self.r // 2, self.otstH + self.h // 2 + self.r // 2))
        self.sc.blit(self.n_scale, self.n_rect)
        self.c_W = self.otstW + self.w // 2
        self.c_H = self.otstH + self.h // 2
        self.r = self.r

    def bigger(self):
        pygame.draw.rect(self.sc, (0, 0, 0),(self.otstW, self.otstH, self.w, self.h) )
        self.n_scale = pygame.transform.scale(self.n_surf, ((int)(self.r * 1.1), (int)(self.r * 1.1)))
        self.n_rect = self.n_scale.get_rect(
            bottomleft=(self.otstW + self.w // 2 - self.r * 1.1 // 2, self.otstH + self.h // 2 + self.r * 1.1 // 2))
        self.sc.blit(self.n_scale, self.n_rect)

    def smaller(self):
        pygame.draw.rect(self.sc, (0, 0, 0), (self.otstW, self.otstH, self.w, self.h))
        self.n_scale = pygame.transform.scale(self.n_surf, (self.r, self.r))
        self.n_rect = self.n_scale.get_rect(
            bottomleft=(self.otstW + self.w // 2 - self.r // 2, self.otstH + self.h // 2 + self.r // 2))
        self.sc.blit(self.n_scale, self.n_rect)