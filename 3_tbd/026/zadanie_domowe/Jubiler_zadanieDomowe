
from flask import Flask, render_template, redirect, url_for
import sys
import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import random


from moje_programy.character_wiki import osobnik
from moje_programy.open_poem import open_poem




sys.path.append('/home/jubiler/backup/flaga/templates')
from moje_programy.haslo import gen_hasla

app=Flask(__name__)
app.secret_key='xd'


@app.route('/')
def index():
	text = open('dane/xd.txt').read()
	return render_template("index.html", text=text)

@app.route('/kubus_puchatek')
def kubus_puchatek():
	return render_template("kubus_puchatek.html")

@app.route('/generator_hasla')
def geeratorn_hasla():
	return render_template("generator_hasla.html", text=gen_hasla())

@app.route('/xd')
def flaga_xD():
	text = open('dane/flaga_xd.txt').read()
	return render_template('flaga_xd.html',text=text)



@app.route('/flaga_dla_ukrainy')
def flaga_UA():
	
	return render_template('UA.html')


@app.route('/brudnopis')
def brudnopis():
	imie = ['Xi Jinping', 'Tarnobrzeg', 'Adam Małysz']
	wiersz = open_poem()
	chosen_char = random.choice(imie)
	super_hero= osobnik(chosen_char)
	return render_template('brudnopis.html',wiersz= wiersz,hero = super_hero, imie = imie  )


@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    list_of_heroes = [
        'Pudzianowski',         # 0
        'Małysz',               # 1
        'Kopernik',             # 2
        'Maria Skłodowska',     # 3
        'Kościuszko',           # 4
        'Donald',               # 5
        'Myszka Miki',          # 6
    ]
    heroes_desc = []
    for i in range(3):
        hero = random.choice(list_of_heroes)
        indeks = list_of_heroes.index(hero)
        list_of_heroes.pop(indeks)

        char_desc = osobnik(hero)
        desc_len = len(char_desc)
        words_num =len(char_desc.split())
        info = [hero, char_desc, desc_len,words_num]
        heroes_desc.append(info)

    heroes_desc.sort(key=lambda x:x[3], reverse=True)

    return render_template("ciekawePostacie.html", heroes_desc=heroes_desc)
	

# formularze z 26 IV

@app.route('/form_a', methods=["GET", "POST"])
def form_a():

    form = X()
    if form.validate_on_submit():
        
        github = form.github.data
        my_github_state = form.my_github_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(github, my_github_state, follow_me)
        #save_data(string)

        return redirect( url_for('form_result'))

    return render_template("form_a.html", form=form)

@app.route('/form_b', methods=["GET", "POST"])
def form_b():
    form = Y()
    if form.validate_on_submit():
        
        musiclink = form.musiclink.data
        genre = form.genre.data
        sweares = form.sweares.data

        string = '{}\n{}\n{}\n\n'.format(musiclink, genre, sweares)
        #save_data(string)

        return redirect( url_for('form_b_result'))

    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")

@app.route('/form_b_result')
def form_b_result():
    return render_template("form_b_result.html")

# Helpers

def save_data(string):
    with open('data/data.txt', "a") as f:
        f.write(string)


# Errors

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500


# Form

class X(FlaskForm):
    x_options = [
            ('a','a'),
            ('b','b'),
            ('c','c'),
            ('d','d'),
    ]

    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('kk')


class Y(FlaskForm):
    y_options = [
            ('a','metal'),
            ('b','rock'),
            ('c','indie'),
            ('d','disco'),
            ('e','folktronika'),
            ('f','inne'),
    ]

    musiclink = StringField('Polecana nutka:', validators=[DataRequired()])
    genre = SelectField('Co to za gatunek:', choices=y_options)
    sweares = BooleanField('Obiecujesz, że bez przekleństw?')

    button = SubmitField('Podaj DJowi')

#koniec formularzy



if __name__=="__main__":
	app.run(debug=True)
    
