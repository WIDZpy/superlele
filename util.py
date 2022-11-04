import pickle
import tkinter as tk
import tkinter.ttk as ttk
from pprint import pprint

import matplotlib.pyplot as plt


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
		pprint(lst)
		return lst


def init_fille(fille_name: str = 'save'):
	with open(fille_name, 'wb') as wf:
		pickle.dump([], wf)


def save_new(lst: 'list', fille: str = 'save'):
	new_fill = read_fille(fille).append(lst)
	with open(fille, 'wb') as wf:
		pickle.dump(new_fill, wf)


if __name__ == '__main__':
	init_fille('save_fps')
