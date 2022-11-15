import pickle
import pygame as pg
from util import ProgressBar, save_new, rand_color


def func(title: str = '', itration: int = 1, save_fille_name: str = 'save_squars_corods', save_fps_fille_name: str = 'save_fps'):
    progres = ProgressBar()

    pg.init()
    tail = (790, 400)
    win = pg.display.set_mode(tail)
    a, b, c, d = rect = [0, 0, 100, 100]
    color = (255, 255, 255)
    x = 0
    y = 0

    run = raar = itration
    t = pg.time.Clock()
    surf_trace = pg.surface.Surface(tail)
    speed = 10
    cot = 10



    co = 0

    ar = []
    fps = [title]


    while run != 0:
        co += 1
        t.tick(1000)

        if pg.event.get(pg.QUIT):
            run = False
        carre_rect = pg.rect.Rect((x, y, 50, 70))
        litle_squar = pg.rect.Rect((carre_rect.center[0]-cot, carre_rect.center[1]-cot, 2*cot, 2*cot))
        pg.draw.rect(win, color, (carre_rect.center[0]-cot, carre_rect.center[1]-cot, 2*cot, 2*cot))

        if carre_rect.x == 0 and carre_rect.y == 0:
            run -= 1
            progres.progres(run, raar)

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
        fps.append(t.get_fps())
        ar.append([litle_squar, color, co])

        pg.display.update()

        win.fill((0, 0, 0))

	save_new(fps, save_fps_fille_name)

    with open(save_fille_name, 'wb') as f:
        pickle.dump(ar, f)

    with open(save_fille_name, 'rb') as f1:
        OL = pickle.load(f1)


if __name__ == '__main__':
    func(itration=50)
    input()
