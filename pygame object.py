import numpy as np
import pygame as pg


class Quadrillage:
	def __init__(self, size):
		self.array = np.zeros(size)

	def fill(self):
		self.array.fill(1)
		return self.array



if __name__ == '__main__':
	a = Quadrillage((10, 10))
	print(a.fill())



