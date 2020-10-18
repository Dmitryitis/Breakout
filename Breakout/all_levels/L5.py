from Breakout.models.Mobs import Mobs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
w = 70
d = 25
class L5:
    def __init__(self, mobs, all_sprites, all_bricks):
        self.mobs = mobs
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks

    def writePix(self, w_num, d_num, color):
        m = Mobs(color, w, d)
        m.rect.x = 15 + w * w_num
        m.rect.y = 60 + d * d_num
        self.mobs.add(m)
        self.all_sprites.add(m)
        self.all_bricks.add(m)

    def start(self):
        i = 0
        for j in (3, 4, 6, 7):
            self.writePix(j, i, "blue")

        for i in (1, 7):
            for j in range(2, 9):
                self.writePix(j, i, "blue")

        for i in (2, 6):
            for j in range(1, 10):
                self.writePix(j, i, "blue")

        for i in (3, 4, 5):
            for j in range(0, 11):
                self.writePix(j, i, "blue")

        i = 8
        for j in range(3, 8):
            self.writePix(j, i, "blue")

        i = 9
        for j in range(4, 7):
            self.writePix(j, i, "blue")

        i = 10
        self.writePix(5, i, "blue")

        for i in range(2, 9):
            self.writePix(5, i, "white")

        self.writePix(4, 2, "white")
        self.writePix(6, 2, "white")
        self.writePix(4, 8, "white")
        self.writePix(6, 8, "white")









