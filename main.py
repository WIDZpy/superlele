import pickle
from pprint import pprint
import pygame as pg
from random import randint
from tkinter import *
from tkinter.ttk import *

root = Tk()
progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
progress.pack(pady=10)

pg.init()
tail = (790, 400)
win = pg.display.set_mode(tail)
a, b, c, d = rect = [0, 0, 100, 100]
color = (255, 255, 255)
x = 0
y = 0

run = raar = 30
t = pg.time.Clock()
surf_trace = pg.surface.Surface(tail)
speed = 10
cot = 10


def rand_color():
    color_random = randint(0, 255), randint(0, 255), randint(0, 255)
    return color_random


co = 0

ar = []

while run != 0:
    progress['value'] = 100 - run/raar * 100
    root.update()
    co += 1
    t.tick(1000)

    if pg.event.get(pg.QUIT):
        run = False
    carre_rect = pg.rect.Rect((x, y, 50, 70))
    pg.draw.rect(surf_trace, color, (carre_rect.center[0]-cot, carre_rect.center[1]-cot, 2*cot, 2*cot))
    win.blit(surf_trace, (0, 0))
    pg.draw.rect(win, (0, 0, 0), carre_rect)

    if carre_rect.x == 0 and carre_rect.y == 0:
        run -= 1

    if (carre_rect.x <= 0 or carre_rect.x >= win.get_size()[0]-carre_rect.width) or (carre_rect.y <= 0 or carre_rect.y >= win.get_size()[1] - carre_rect.height):
        color = rand_color()

    if x >= tail[0]-carre_rect.width:
        a = -1
    elif x <= 0:
        a = 1

    if y >= tail[1] - carre_rect.height:
        b = -1
    elif y <= 0:
        b = 1
    x += a*speed
    y += b*speed
    print('\r', x, y, t, end='')

    ar.append([carre_rect, color, co])

    pg.display.update()

    win.fill((0, 0, 0))

with open('fill', 'wb') as f:
    pickle.dump(ar, f)

with open('fill', 'rb') as f1:
    OL = pickle.load(f1)
pprint(OL)
