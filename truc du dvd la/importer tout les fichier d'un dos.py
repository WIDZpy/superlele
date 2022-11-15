import importlib as imp
from os import listdir
from os.path import isfile, join
import util as u


progres = u.ProgressBar()


def func(mon_repertoire):
	save_fpd_fill = 'save_fps'
	u.init_fille(save_fpd_fill)
	fichiers = [f[:-3] for f in listdir(mon_repertoire) if isfile(join(mon_repertoire, f)) and f != '__init__.py']
	nb_of_fill = len(fichiers)
	for fille in fichiers:
		imp.import_module(mon_repertoire + '.' + fille, mon_repertoire).func(fille, 20, save_fps_fille_name=save_fpd_fill)
		progres.progres(len(fichiers)-nb_of_fill, len(fichiers))
		nb_of_fill -= 1

	u.afiche_graphe(u.read_fille('save_fps'), moy='')


if __name__ == '__main__':
	func('tout_les_posibiliter_a_tester')
