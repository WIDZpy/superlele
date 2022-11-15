import pygame as pg

pg.init()
win = pg.display.set_mode((600, 600))


def b_cord(pos_1, pos_2, proportion=0.5):
	return pos_1[0]+((pos_2[0] - pos_1[0]) * proportion), pos_1[1]+((pos_2[1] - pos_1[1]) * proportion)

time = pg.time.Clock()

count = 0
point_1 = (100, 100)
point_2 = (200, 200)
point_3 = (50, 500)

surf = pg.Surface(win.get_size(),pg.SRCALPHA)


def true_baiser(list_point, propor):
	if len(list_point) == 2:
		pg.draw.line(win, (255, 0, 0), *list_point)
		p = b_cord(*list_point, propor)
		pg.draw.circle(win, (0, 0, 255), p, 3)
		return b_cord(*list_point, propor)
	else:
		p_2 = true_baiser(list_point[1:], propor)

		p_1 = true_baiser(list_point[:-1], propor)

		pg.draw.line(win, (0, 255, 0), p_1, p_2)
		p_3 = b_cord(p_1, p_2, propor)
		pg.draw.circle(win, (0, 255, 255), p_3, 3)
		return p_3












while True:
	if pg.event.get(pg.QUIT):
		break
	
	prop = (count % 300+1)/300
	#prop = 0.5

	time.tick(40)
	#pg.draw.circle(surf, (255, 255, 255), true_baiser([(20, 500),(500, 500),(20, 20)], prop), 1)

	pg.draw.circle(surf, (255, 255, 255), true_baiser([(20, 20), (20, 580), (580, 580), (580, 20), (20, 20), (20, 580), (580, 580), (580, 20), (20, 20), (20, 580), (580, 580), (580, 20), (20, 20), (20, 580), (580, 580), (580, 20), (20, 20)], prop), 1)
	pg.display.update()
	win.fill((0, 0, 0))
	win.blit(surf, (0, 0))
	count += 1


a = False
if a:
	pg.draw.line(win, (255, 0, 0), point_1, point_2)
	pg.draw.line(win, (255, 0, 0), point_2, point_3)
	pg.draw.line(win, (0, 255, 0), b_cord(point_1, point_2, prop), b_cord(point_2, point_3, prop))

	pg.draw.circle(win, (255, 255, 255), b_cord(point_2, point_3, prop), 5)
	pg.draw.circle(win, (255, 255, 255), b_cord(point_1, point_2, prop), 5)
	pg.draw.circle(surf, (255, 0, 255), b_cord(b_cord(point_1, point_2, prop), b_cord(point_2, point_3, prop), prop), 2)

	win.blit(surf, (0, 0))
	pg.draw.circle(win, (0, 0, 255), b_cord(b_cord(point_1, point_2, prop), b_cord(point_2, point_3, prop), prop), 3)