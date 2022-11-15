import pickle
import tkinter as tk
import tkinter.ttk as ttk
from pprint import pprint
from random import randint

import matplotlib.pyplot as plt
import numpy as np


def rand_color():
	color_random = randint(0, 255), randint(0, 255), randint(0, 255)
	return color_random


class ProgressBar:
	def __init__(self):
		self.root = tk.Tk()
		self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=1000, mode='determinate')
		self.progress.pack(pady=10)

	def progres(self, valu, total):
		"""
        :param valu:
        :param total:
        :return:
        """
		self.progress['value'] = 100 - valu / total * 100
		self.root.update()


def read_fille(fille: str = "fill") -> list:
	with open(fille, 'rb') as f:
		lst = pickle.load(f)
	return lst


def init_fille(fille_name: str = 'save'):
	with open(fille_name, 'wb') as wf:
		pickle.dump([], wf)


def save_new(element, fille: str = 'save'):
	new_fill = read_fille(fille)
	new_fill.append(element)
	with open(fille, 'wb') as wf:
		pickle.dump(new_fill, wf)


def afiche_graphe(lst: 'list', moy: bool = False):
	l = []
	for game in lst:
		if moy == True:
			a = np.array(game[1:])
			a.fill(a.mean())
			pprint(a)
			plt.plot(np.arange(len(game) - 1), a, label=game[0])
		elif moy == False:
			plt.plot(np.arange(len(game) - 1), game[1:], label=game[0])
		else:
			a = np.array(game[1:])
			a.fill(a.mean())
			pprint(a)
			plt.plot(np.arange(len(game) - 1), a, label=game[0])
			plt.plot(np.arange(len(game) - 1), game[1:], label=game[0])
	plt.legend()
	plt.show()


if __name__ == '__main__':
	afiche_graphe(read_fille('save_fps'), moy=True)
	# print(read_fille('save_fps'))
	# save_new([1, 1], 'save_fps')
	# print(read_fille('save_fps'))
