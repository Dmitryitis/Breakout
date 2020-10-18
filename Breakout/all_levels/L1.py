from Breakout.Mobs import Mobs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
w = 70
d = 25
class L1:
    def __init__(self, mobs, all_sprites, all_bricks):
        self.mobs = mobs
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks

    def writePix(self, x, y, color):
        m = Mobs(color, 70, 25)
        m.rect.x = x
        m.rect.y = y
        self.mobs.add(m)
        self.all_sprites.add(m)
        self.all_bricks.add(m)

    def start(self):


        for i in range(11):
            self.writePix(10 + i * w, 60, "yellow")

        for i in range(11):
            self.writePix(10 + 10 * w, 60 + i * d + d, "blue")

        for i in range(10):
            self.writePix(10 + i * w, 60 + 10 * d + d, "green")

        for i in range(10):
            self.writePix(10, 60 + 2 * d + d * i, "red")


        for i in range(8):
            self.writePix(10 + i * w + w, 60 + 2 * d, "yellow")

        for i in range(7):
            self.writePix(10 + 8 * w, 60 + 3 * d + i * d, "blue")

        for i in range(6):
            self.writePix(10 + i * w + w * 2, 60 + 9 * d, "green")

        for i in range(5):
            self.writePix(10 + w * 2, 60 + 4 * d + d * i, "red")

        for i in range(4):
            self.writePix(10 + i * w + 3 * w, 60 + 4 * d, "yellow")

        for i in range(3):
            self.writePix(10 + 6 * w, 60 + i * d + 5 * d, "blue")

        for i in range(2):
            self.writePix(10 + 4 * w + i * w, 60 + 7 * d, "green")

        for i in range(1):
            self.writePix(10 + 4 * w + i * w, 60 + 6 * d, "red")




