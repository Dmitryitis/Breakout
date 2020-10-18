import pygame

W = 800
H = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Mobs(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        br_surf = pygame.image.load("images/mobs/" + color + ".png")
        br_scale = pygame.transform.scale(br_surf, (width, height))
        br_rect = br_scale.get_rect(bottomleft=(0, height))
        self.image.blit(br_scale, br_rect)


        self.rect = self.image.get_rect()

    def score_update(self):
        score_up = 5
        if self.color == RED:
            score_up = 15
        if self.color == YELLOW:
            score_up = 10
        return score_up
