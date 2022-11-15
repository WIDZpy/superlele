from pprint import pprint
import cv2
import numpy as np

from util import read_fille
import pygame as pg
import pickle

test_img = cv2.imread('Sans titre.png')
print(test_img.dtype)



def play_list(lst):
	win = pg.display.set_mode((790, 400))
	video = cv2.VideoWriter('video7.avi', cv2.VideoWriter_fourcc(*'mp4'), 60, win.get_size())
	for frame in lst:
		print('caca')
		pg.draw.rect(win, frame[1], frame[0])
		pg.display.update()
		b = pg.surfarray.array3d(win).astype(np.uint8)
		print(b.shape)
		video.write(b.transpose((1, 0, 2)))

	print('loop')
	cv2.destroyAllWindows()
	video.release()


if __name__ == '__main__':

	# play_list(read_fille("save_squars_corods"))
	play_list(read_fille('finale_'))

