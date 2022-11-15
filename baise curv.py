import pygame as pg
from math import sin, cos, radians


pg.init()
win = pg.display.set_mode((600, 600))
count = 0
prop = 0


def b_cord(pos_1, pos_2, proportion=0.5):
	return pos_1[0]+((pos_2[0] - pos_1[0]) * proportion), pos_1[1]+((pos_2[1] - pos_1[1]) * proportion)

time = pg.time.Clock()

surf = pg.Surface(win.get_size(),pg.SRCALPHA)

def true_baiser(list_point, propor):
	if len(list_point) == 2:
		pg.draw.line(win, (255,255,255),*list_point)
		b = b_cord(*list_point, propor)
		pg.draw.circle(win, (255, 0, 0), b, 5)
		return b

	lst_rep = []
	for seg in range(len(list_point)-1):
		lst_rep.append(b_cord(list_point[seg], list_point[seg+1], propor))
		pg.draw.circle(win, (255, 150, 150), b_cord(list_point[seg], list_point[seg+1],propor), 5)

		pg.draw.line(win, (255, 255, 255), list_point[seg], list_point[seg+1])
	p = true_baiser(lst_rep, propor)
	return p


def poligonne_coord(nb, l, pos, repet = 1):
	rep = []
	for loop in range(nb):
		angle = radians((360*loop)/nb)
		rep.append((l*cos(angle)+pos[0],l*sin(angle)+pos[1]))
	return rep*repet + [rep[0]]

h=true_baiser(poligonne_coord(6, 300, (300, 300), 1), prop)

while True:
	if pg.event.get(pg.QUIT):
		break



	prop = (count % 500+1)/500

	# prop = 0.1

	time.tick(40)

	a = true_baiser(poligonne_coord(20, 300, (300, 300), 5), prop)

	pg.draw.line(surf, (0, 255, 255), h, a, 3)

	h = a

	win.blit(surf, (0, 0))
	pg.display.update()
	win.fill((0, 0, 0))
	count += 1