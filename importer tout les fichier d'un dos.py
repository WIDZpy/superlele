import importlib as imp
from os import listdir
from os.path import isfile, join
import util as u

progres = u.ProgressBar()


def func(mon_repertoire):
	fichiers = [f[:-3] for f in listdir(mon_repertoire) if isfile(join(mon_repertoire, f)) and f != '__init__.py']
	for fille in fichiers:
		imp.import_module(mon_repertoire + '.' + fille, mon_repertoire).func(fille, 30)


if __name__ == '__main__':
	func('tout_les_posibiliter_a_tester')
