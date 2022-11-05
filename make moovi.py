from pprint import pprint
import cv2
from util import read_fille
import pygame as pg
import pickle

test_img = cv2.imread('Sans titre.png')
print(test_img.dtype)

video = cv2.VideoWriter('video5.avi', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 1, test_img.shape[:2])



def play_list(lst):
	win = pg.display.set_mode([1, 1])
	for frame in lst:
		print('caca')
		pg.draw.rect(win, frame[1], frame[0])
		pg.display.update()
		b = pg.surfarray.array3d(win)
		print(type(b))
		video.write(test_img)
	print('loop')
	cv2.destroyAllWindows()
	video.release()



if __name__ == '__main__':

	# play_list(read_fille("save_squars_corods"))
	play_list(read_fille('test_fille'))
