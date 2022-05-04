from flask import Flask, render_template

import random
import os
import wikipedia
import requests
from lxml import html


app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'


@app.route('/flaga', methods=["GET", "POST"])
def flaga():
	create_folders()

	# Flag.
	xd = random.choice(range(22))
	if len(os.listdir('static/flag_image')) < 10:
		xd = 11
	ta_flaga = os.path.join(app.config['UPLOAD_FOLDER'], 'Polska_Flaga__{}.jpg'.format(xd))
	
	# Gather heroes.
	heroes = gather_heroes()
	random.shuffle(heroes)

	return render_template("flaga.html", xd=xd, flaga=ta_flaga, heroes=heroes)

def gather_heroes():
	
	heroes = [
 		'Mikołaj Kopernik', 
 		'Rotmistrz Pilecki',
 		'Maria Skłodowska',
 		'Fryderyk Chopin',
		
 		#'Józef Piłsudski'
 		#'Tadeusz Kościuszko',
 		#'Adam Mickiewicz',
 		
		#'Jan Henryk Dąbrowski',
 		# 'Józef Haller',
 		# 'Władysław Sikorski',
		# 'Wojciech Korfanty',
 		# 'Mieczysław Paluch',
		
	]

	greetings = [
		'pozdrawia',
		'/wave',
		'/wink',
		'wita',
	]

	wikipedia.set_lang("pl")

	saved_heroes = os.listdir('saved_heroes')
	saved_heroes = [h.split('.')[0] for h in saved_heroes]

	for hero in heroes:
		if hero not in saved_heroes:

			# Get some info and link.
			some_info = wikipedia.page(hero)
			info_intro = some_info.content.split('\n\n')[0]
			url = '<a href="'+some_info.url+'">Poszukaj więcej info o: '+hero+"</a>"
			
			# Get what hero thinks.
			hero_think(hero)
			
			# Get & save images.
			# images = some_info.images
			# n_photos = 0
			# for i, image_url in enumerate(images):
			# 	if i < 3:
			# 		hero_str = '11'.join(hero.split())
			# 		image_name = '{}_{}.legend'.format(hero_str, i)
			# 		save_image(image_url, image_name)
			# 		n_photos += 1

			# Save all.
			with open('saved_heroes/'+hero+".hero", "w+") as f:
				f.write(hero + '\n')
				f.write('\n') #str(n_photos) + '\n')
				f.write(info_intro + '\n')
				f.write(url)

		else:
			greeting = random.choice(greetings)
			print(hero, greeting)

	heroes = []
	for hero_file in os.listdir('saved_heroes'):
		hero = {}
		some_info = open('saved_heroes/'+hero_file).readlines()
		hero['name'] = some_info[0]
		#photo_nr = random.choice(range(int(some_info[1])))
		#hero_str = '11'.join(hero['name'][:-1].split())
		#hero['image'] = '{}_{}.legend'.format(hero_str, photo_nr)
		hero_quotes = open('hero_think/' + hero['name'][:-1] + ".hero").readlines()
		hero['quote'] = random.choice(hero_quotes)
		hero['description'] = '\n'.join(some_info[2:-1])
		hero['description'] = bold(hero['description'])
		hero['url'] = some_info[-1]
		heroes.append(hero)

	return heroes

# def save_image(image_url, image_name):
# 	image = requests.get(image_url).content
# 	save_as = 'static/hero_image/{}'.format(image_name)
# 	with open(save_as, 'wb') as ap:
# 		ap.write(image)
# 	return save_as

def bold(hero_info):

	nice = [
		'nauk',
		'gen',
		'zwy',
		'odk',
		'zał',
		'rod',
		'organizator',
		'astronom',
		'inżynier',
		'herbu',
		'wojska',
		'uczona',
		'nobla',
		'wybitniej',
		'romantyczny',
		'fizyk',
		'filozof',
		'kocha',
		'woli',
		'kawalerii',
		'skazany',
	]

	right_desc = []
	words = [w.lower() for w in hero_info.split()]
	for w in words:
		for woah in nice:
			if w.startswith(woah):
				w = '<b>'+w+'</b>'
		right_desc.append(w)
	right_desc = " ".join(right_desc)
	return right_desc

def hero_think(name):
	url_name = name.replace(' ', '_')
	url = 'https://pl.wikiquote.org/wiki/{}'.format(url_name)
	hero_wikiquotes = requests.get(url)
	with open('hero_think/'+name+".hero", "w+") as f:
		
		for line in hero_wikiquotes.text.split('\n'):
			if line.startswith('<h2>O'):
				continue
			if line.startswith('<ul><li>'):
				
				tree = html.fromstring(line)
				quote = tree.text_content().strip()
				
				if not quote.startswith('Opis') and not quote.startswith('Autor') and not quote.startswith('Źródło'): 
					f.write(quote + '\n')
					print('-', quote)

def create_folders():
	os.system("mkdir static/hero_image")
	os.system("mkdir static/flag_image")
	os.system("mkdir saved_heroes")
	os.system("mkdir hero_think")


if __name__ == "__main__":
	app.run(debug=True)
