import pygame as pg
from random import randint
pg.init()
tail = (790, 400)
win = pg.display.set_mode(tail)
a,b,c,d = rect = [0,0,100,100]
color = (255, 255, 255)
x = 0
y = 0
run = True
t = pg.time.Clock()
surf_trace = pg.surface.Surface(tail)
speed = 10
cot = 10
def rand_color():
    c = randint(0,255) , randint(0,255) , randint(0,255)
    return c

while run:

    # t.tick(100)

    if pg.event.get(pg.QUIT):
        run = False
    carre_rect = pg.rect.Rect((x, y, 50, 70))
    pg.draw.rect(surf_trace, color, (carre_rect.center[0]-cot, carre_rect.center[1]-cot, 2*cot, 2*cot))
    win.blit(surf_trace, (0, 0))
    # pg.draw.rect(win, color, carre_rect)

    print(carre_rect.x, carre_rect.width)

    if carre_rect.x == 0 and carre_rect.y == 0:
        input()



    if (carre_rect.x <= 0 or carre_rect.x >= win.get_size()[0]-carre_rect.width) or (carre_rect.y <= 0 or carre_rect.y >= win.get_size()[1]- carre_rect.height):
        color = rand_color()

    if x >= tail[0]:
        a = -1
    elif x <= 0:
        a = 1

    if y >= tail[1]:
        b = -1
    elif y <= 0:
        b = 1
    x += a*speed
    y += b*speed
    print('\r',x,y, t,end='')


    pg.display.update()
    win.fill((0,0,0))
