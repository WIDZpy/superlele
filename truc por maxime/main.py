dic = {
	"pos": '[64R,64]',
	"size": '[64,64]',
	"bg": "ffffff",
}


def read(cle: str, default: str) -> dict:
	contenu_cle = dic.get(cle, default)

	if contenu_cle[0] == "[":
		nb = 1
		int_valu = []
		mod_valu = []

		for _ in 1, 2:
			string_of_number = ''

			while contenu_cle[nb].isnumeric():
				string_of_number += contenu_cle[nb]
				nb += 1

			if string_of_number != '':
				int_valu.append(int(string_of_number))

			if cle in ['pos']:  # list des élément qui ont un mode
				if contenu_cle[nb] in [",", "]"]:
					mod_valu.append("A")
				else:
					mod_valu.append(contenu_cle[nb])

				nb += 1

			nb += 1

		if cle == 'pos':
			return {
				'pos': int_valu,
				'mod': mod_valu
			}

		if cle == 'size':
			return {'size': int_valu}

	return {cle: contenu_cle}


if __name__ == '__main__':
	print(read('pos', '[0R,0R]'))
	print(read('size', '[100,100]'))
	print(read('color', 'ffffff'))
	print(read('prénom', 'raphael'))
	print(read('sizeeee', '[10,10]'))

