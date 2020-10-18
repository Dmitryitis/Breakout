from Breakout.models.Mobs import Mobs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
w = 70
d = 25
class L2:
    def __init__(self, mobs, all_sprites, all_bricks):
        self.mobs = mobs
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks

    def writePix(self, color, x, y):
        m = Mobs(color, 70, 25)
        m.rect.x = x
        m.rect.y = y
        self.mobs.add(m)
        self.all_sprites.add(m)
        self.all_bricks.add(m)

    def start(self):
        for j in range(3):
            for i in range(11 - 4 * j):
                self.writePix("yellow",  15 + i * w + (j * 2 * w), 60 + 4 * j * d)
            for i in range(10 - 4 * j):
                self.writePix("red", 15 + w // 2 + i * w + (j * 2 * w), 60 + d + 4 * j * d)
            for i in range(9 - j * 4):
                self.writePix("green", 15 + i * w + w + (j * 2 * w), 60 + 2 * d + 4 * j * d)
            for i in range(8 - j * 4):
                self.writePix("blue", 15 + i * w + w // 2 * 3 + (j * 2 * w), 60 + 3 * d + 4 * j * d)