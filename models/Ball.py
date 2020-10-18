import math

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


class Ball(pygame.sprite.Sprite):
    direction = 180
    speed = 4
    x = 380.0
    y = 460.0

    width = 20
    height = 20

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = self.x
        self.rect.y = self.y

    def bouncy(self, diff):
        self.direction = (180 - self.direction) % 360

        self.direction -= diff


    def speed_bot(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.speed = 12
        else:
            self.speed = 8

    def update(self):
        self.speed_bot()
        direction_radians = math.radians(self.direction)

        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0:
            self.bouncy(0)
            self.y = 1

        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1

