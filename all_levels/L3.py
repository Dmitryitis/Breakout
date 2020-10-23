from models.Mobs import Mobs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
class L3:
    def __init__(self, mobs, all_sprites, all_bricks, bricks_group):
        self.mobs = mobs
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks
        self.bricks_group = bricks_group

    def writePix(self, x, y, color):
        m = Mobs(color, 70, 25)
        m.rect.x = x
        m.rect.y = y
        self.mobs.add(m)
        self.all_sprites.add(m)
        self.all_bricks.add(m)
        self.bricks_group.add(m)

    def start(self):
        for j in range(2):
            for i in range(11):
                self.writePix(15 + i * 70, 60 + j * 100, "yellow")
            for i in range(11):
                self.writePix(15 + i * 70, 85 + j * 100, "red")
            for i in range(11):
                self.writePix(15 + i * 70, 110 + j * 100, "green")
            for i in range(11):
                self.writePix(15 + i * 70, 135 + j * 100, "blue")
