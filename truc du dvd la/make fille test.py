import time

import util as u
import pygame as pg
import random as r
u.init_fille('test_fille')
win = pg.display.set_mode((100, 100))

for frame in range(10):
	rect =(r.randint(0, 90), r.randint(0, 90), 10, 10)
	pg.draw.rect(win, (255, 255, 255), rect)
	u.save_new([rect, (255, 255, 255)], 'test_fille')
	time.sleep(1)
	pg.display.update()


# for frame in range(10):
# 	pg.draw.rect(win, (255, 255, 255), (r.randint(0, 90), r.randint(0, 90), 10, 10))
# 	u.save_new(pg.surfarray.pixels3d(win), 'test_fille')
# 	time.sleep(1)
# 	pg.display.update()
