from Breakout.models.Mobs import Mobs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
w = 66
d = 25
class L4:
    def __init__(self, mobs, all_sprites, all_bricks):
        self.mobs = mobs
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks

    def writePix(self, w_num, d_num, color):
        m = Mobs(color, w, d)
        m.rect.x = 4 + w * w_num
        m.rect.y = 60 + d * d_num
        self.mobs.add(m)
        self.all_sprites.add(m)
        self.all_bricks.add(m)

    def start(self):
        i = 0
        self.writePix(0, i, "red")
        self.writePix(1, i, "red")
        self.writePix(10, i, "red")
        self.writePix(11, i, "red")

        i = 1
        self.writePix(0, i, "red")
        self.writePix(2, i, "red")
        self.writePix(9, i, "red")
        self.writePix(11, i, "red")

        i = 2
        for j in range(3, 9):
            self.writePix(j, i, "red")

        i = 3
        self.writePix(3, i, "red")
        self.writePix(2, i, "red")
        self.writePix(9, i, "red")
        self.writePix(8, i, "red")
        for j in range(4, 8):
            self.writePix(j, i, "green")

        for i in range(4, 9):
            self.writePix(2, i, "red")
            self.writePix(9, i, "red")
            for j in range(3, 9):
                self.writePix(j, i, "green")
                self.writePix(j, i, "green")
        i = 9
        self.writePix(3, i, "red")
        self.writePix(5, i, "red")
        self.writePix(8, i, "red")
        self.writePix(6, i, "red")
        self.writePix(4, i, "green")
        self.writePix(7, i, "green")

        for i in range(10, 15):
            self.writePix(4, i, "red")
            self.writePix(7, i, "red")
        i = 14
        self.writePix(3, i, "red")
        self.writePix(8, i, "red")

        i = 5
        self.writePix(4, i, "blue")
        self.writePix(7, i, "blue")

        i = 7
        self.writePix(5, i, "yellow")
        self.writePix(6, i, "yellow")











