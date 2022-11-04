from pprint import pprint
from util import read_fille
import pygame as pg
import pickle


def play_list(lst):
	win = pg.display.set_mode((790, 400))
	for frame in lst:
		pg.draw.rect(win, frame[1], frame[0])
		pg.display.update()
	input()


read_fille()

play_list(read_fille("save_squars_corods"))
