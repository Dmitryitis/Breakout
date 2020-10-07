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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 75
        self.height = 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, GREEN, (0, 0, self.width, self.height))

        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.rect.x = W // 2 -25
        self.rect.y = self.screenheight - self.height
        self.speed = 12

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.rect.x -= self.speed
        # else:
        #     pos = pygame.mouse.get_pos()
        #     self.rect.x = pos[0]

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > W:
            self.rect.right = W
