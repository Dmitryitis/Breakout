import pygame

from Breakout.Levels import Levels


def isPointUnder(p1, p2, p):
    k = (p1[1] - p2[1]) / (p1[0] - p2[0])
    b = p1[1] - k * p1[0]
    if k * p[0] + b < p[1]:
        return True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (120, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

ON_START = 1
ON_LEVELS = 2
NOT = 0
motion = NOT
pr_motion = NOT

W = 800
H = 600
FPS = 60
#вспомогательные числа
otstW = (int)(W / 6.4)
dW = (int)(W / 8)
dW_sm = (int) (W / 16)
otstH = (int)(H / 3)
dH = (int)(H / 12)
dH_sm = (int)(H / 24)
t_middle = H - otstH
#точки фигуры старт
p1_s = [otstW, t_middle]
p2_s = [otstW + dW, t_middle - dH]
p3_s = [W - otstW - dW, t_middle - dH]
p4_s = [W - otstW, t_middle]
p5_s = [W - otstW - dW, t_middle + dH]
p6_s = [otstW + dW, t_middle + dH]

p1_l = [dW_sm * 5, H - dH * 2]
p2_l = [otstW + dW, H - dH * 2 - dH_sm]
p3_l = [W - otstW - dW, H - dH * 2 - dH_sm]
p4_l = [W - dW_sm * 5, H - dH * 2]
p5_l = [W - otstW - dW, H - dH * 2 + dH_sm]
p6_l = [otstW + dW, H - dH * 2 + dH_sm]


pygame.init()

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

def making_picture(sc):
    br_surf = pygame.image.load(r'images\2.png')
    br_scale = pygame.transform.scale(br_surf, ((int)(br_surf.get_width() * 1.50 * (int)(W / 800)),
                                            (int)(br_surf.get_height() * 1.50) * (int)(H / 600)))
    br_rect = br_scale.get_rect(bottomleft=(0, H))
    sc.blit(br_scale, br_rect)

making_picture(sc)
#иконка START
surf_start_x = p1_s[0]
surf_start_y = p2_s[1]
surf_start = pygame.Surface((p4_s[0] - p1_s[0], p5_s[1] - p3_s[1]))
#надпись
f_start = pygame.font.SysFont(None, 110)
text_start = f_start.render('START', 1, (255, 255, 255))
#фигура
start_figure =[[p1_s[0] - surf_start_x, p1_s[1] - surf_start_y],
            [p2_s[0] - surf_start_x, p2_s[1] - surf_start_y],
            [p3_s[0] - surf_start_x, p3_s[1] - surf_start_y],
            [p4_s[0] - surf_start_x, p4_s[1] - surf_start_y],
            [p5_s[0] - surf_start_x, p5_s[1] - surf_start_y],
            [p6_s[0] - surf_start_x, p6_s[1] - surf_start_y]]
pygame.draw.polygon(surf_start, RED, start_figure)
#наложения
surf_start.blit(text_start, (p2_s[0] - p1_s[0] + 57, 20))
scale_surf_start = pygame.transform.scale(surf_start, ((int)(surf_start.get_width() / 800 * W),
                                           (int)(surf_start.get_height() / 600 * H)))
sc.blit(scale_surf_start, (surf_start_x, surf_start_y))


#иконка LEVELS
surf_level_x = p2_l[0]
surf_level_y = p2_l[1]
surf_level = pygame.Surface((p3_l[0] - p2_l[0], p5_l[1] - p3_l[1]))
#надпись
f_level = pygame.font.SysFont(None, 65)
text_level = f_level.render('LEVELS', 1, (255, 255, 255))
#фигура
level_figure =[[p1_l[0] - surf_level_x, p1_l[1] - surf_level_y],
            [p2_l[0] - surf_level_x, p2_l[1] - surf_level_y],
            [p3_l[0] - surf_level_x, p3_l[1] - surf_level_y],
            [p4_l[0] - surf_level_x, p4_l[1] - surf_level_y],
            [p5_l[0] - surf_level_x, p5_l[1] - surf_level_y],
            [p6_l[0] - surf_level_x, p6_l[1] - surf_level_y]]
pygame.draw.polygon(surf_level, RED, level_figure)
#наложения
surf_level.blit(text_level, (p1_l[0] - p2_l[0] + 67, 5))
scale_surf_level = pygame.transform.scale(surf_level, ((int)(surf_level.get_width() / 800 * W),
                                           (int)(surf_level.get_height() / 600 * H)))
sc.blit(scale_surf_level, (surf_level_x, surf_level_y))

pygame.display.update()

flag = False

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            flag = True
    pos = pygame.mouse.get_pos()

    if (pos[0] >=  p2_s[0] and pos[0] <= p3_s[0] and pos[1] >= p2_s[1] and pos[1] <= p6_s[1]) \
            or (pos[0] <= p2_s[0] and  isPointUnder(p1_s, p2_s, pos) and not isPointUnder(p1_s, p6_s, pos))\
            or (pos[0] >= p3_s[0] and isPointUnder(p3_s, p4_s, pos) and not isPointUnder(p4_s, p5_s, pos)):
        if flag:
            #запуск текущего уровня
            print(1)
            flag = False
        motion = ON_START
    elif (pos[0] >=  p1_l[0] and pos[0] <= p4_l[0] and pos[1] >= p2_l[1] and pos[1] <= p6_l[1]) \
            or (pos[0] <= p1_l[0] and  pos[1] >= p2_l[1] and not isPointUnder(p1_l, p2_l, pos)) \
            or (pos[0] <= p1_l[0] and pos[1] <= p6_l[1] and isPointUnder(p1_l, p6_l, pos)) \
            or (pos[0] >= p4_l[0] and pos[1] >= p2_l[1] and not isPointUnder(p4_l, p3_l, pos)) \
            or (pos[0] >= p4_l[0] and pos[1] <= p6_l[1] and isPointUnder(p4_l, p5_l, pos)):
        if flag:
            print(1)
            levels = Levels(sc, W, H)
            levels.update()
            sc.fill(BLACK)
            making_picture(sc)
            pygame.display.update()
            flag = False
        motion = ON_LEVELS
    else:
        motion = NOT


    if motion is ON_START and pr_motion is not ON_START:
        scale_surf_start_w = scale_surf_start.get_width()
        scale_surf_start_h = scale_surf_start.get_height()
        scale_surf_start_new = pygame.transform.scale(scale_surf_start, ((int)(scale_surf_start_w * 1.1),
                                                               (int)( scale_surf_start_h * 1.1)))
        sc.blit(scale_surf_start_new, (surf_start_x - (int)(scale_surf_start_w * 0.1 // 2), (int)(surf_start_y
                - scale_surf_start_h * 0.1 // 2)))
        pr_motion = ON_START

    if motion is ON_LEVELS and pr_motion is not ON_LEVELS:
        scale_surf_level_w = scale_surf_level.get_width()
        scale_surf_level_h = scale_surf_level.get_height()
        scale_surf_level_new = pygame.transform.scale(scale_surf_level, ((int)(scale_surf_level_w * 1.1),
                                                               (int)( scale_surf_level_h * 1.1)))
        sc.blit(scale_surf_level_new, (surf_level_x - (int)(scale_surf_level_w * 0.1 // 2), (int)(surf_level_y
                - scale_surf_level_h * 0.1 // 2)))
        pr_motion = ON_LEVELS

    if motion is NOT and pr_motion is not NOT:
        pygame.draw.rect(sc, BLACK, (p1_s[0] - (int)((p4_s[0] - p1_s[0]) * 0.1 // 2),
                                    p2_s[1] - (int)((p5_s[1] - p2_s[1]) * 0.1 // 2),
                                     p4_s[0] - p1_s[0] + (int)((p4_s[0] - p1_s[0]) * 0.1),
                                     H - p2_s[1] + (int)((p5_s[1] - p2_s[1]) * 0.1 // 2)))
        sc.blit(scale_surf_level, (surf_level_x, surf_level_y))
        sc.blit(scale_surf_start, (surf_start_x, surf_start_y))
        pr_motion = NOT

    pygame.display.update()

    clock.tick(FPS)