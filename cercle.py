from math import cos, sin, radians

import pygame as pg

win = pg.display.set_mode((700, 700))
center = (350, 350)
angle = 0
clock = pg.time.Clock()
surf = pg.surface.Surface(win.get_size(), pg.SRCALPHA)


class Cercle:
	epeseur = 2
	color_circle = 255, 255, 255
	color_point = 0, 0, 255
	point_radius = 5
	trace_radius = 1
	trace_color = 255, 0 ,0

	def __init__(self, vites, reilon, pos=(350,350), angle=0, parent=None):
		self.pos = pos if parent is None else parent.get_point_pos()
		self.r = reilon
		self.v = vites
		self.parent = parent

		self.angle = angle
		self.point_pos = self.get_point_pos()

	def get_point_pos(self):
		angler = radians(self.angle)
		if self.parent is not None:
			self.pos = self.parent.get_point_pos()

		self.point_pos = (self.pos[0]+cos(angler)*self.r, self.pos[1]+sin(angler)*self.r)
		return self.point_pos

	def draw_circle(self, surf_trace=None):
		self.angle += self.v
		self.angle %= 360
		self.get_point_pos()

		pg.draw.circle(win, Cercle.color_circle, self.pos, self.r + Cercle.epeseur//2, Cercle.epeseur)
		pg.draw.circle(win, Cercle.color_point, self.point_pos, Cercle.point_radius)

		if surf_trace is not None:
			pg.draw.circle(surf_trace, Cercle.trace_color, self.point_pos, Cercle.trace_radius)


size = 100

circle_lst = [Cercle(1, 100, center)]
while size > 10:
	size -= 20
	circle_lst.append(Cercle(size/100, size, parent=circle_lst[-1]))

while True:
	if pg.event.get(pg.QUIT):
		break
	clock.tick(60)

	for loop in circle_lst[:-1]:
		loop.draw_circle()

	circle_lst[-1].draw_circle(surf)

	win.blit(surf, (0, 0))
	pg.display.update()
	win.fill((0, 0, 0))

