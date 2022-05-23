import random
import os
from flask import Flask, render_template
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
from flask import Flask, render_template, redirect, url_for
import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app=Flask(__name__)
app.secret_key = 'abc'

#Main
@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga_dla_ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")

@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Tygrysek', 'Sowa', "Kangurzątko", 'Kłapouchy' ]
    chosen_hero = random.choice( super_heroes)
    super_hero = character( chosen_hero)

    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=super_hero, super_heroes=super_heroes, poem_lines=poem_lines)

@app.route('/ciekawe_postacie')
def ciekawe_postacie():
    lista_ciekawych_postaci = [
        'Anna Jantar',
        'Bill Gates',
        'Muminki',
        'Czerwony Kapturek',]

    opisy_postaci = []
    for i in range(3):
        postac = random.choice(lista_ciekawych_postaci)
        indeks = lista_ciekawych_postaci.index(postac)
        lista_ciekawych_postaci.pop(indeks)
        
        opis_postaci = character(postac)
        ilosc_wyrazow = len(opis_postaci.split())
        info = [postac, opis_postaci, ilosc_wyrazow] 
        opisy_postaci.append(info)

        def wybierz_dluzszy_element(lista):
            return lista[2]
        opisy_postaci.sort(reverse=True)

    return render_template("ciekawe_postacie.html", opisy_postaci=opisy_postaci)  # z flaskwego idzie do html '='

###############    26     ###########################################################

# Forms

@app.route('/form_a', methods=["GET", "POST"])
def form_a():

    form = X()
    if form.validate_on_submit():
        
        github = form.github.data
        my_github_state = form.my_github_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(github, my_github_state, follow_me)
        save_data(string)

        return redirect( url_for('form_result'))

    return render_template("form_a.html", form=form)

@app.route('/form_b')
def form_b():

    form = Y()
    if form.validate_on_submit():
        
        music = form.music_path.data
        my_music_state = form.my_music_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(music, my_music_state, follow_me)
        save_data(string)

        return redirect( url_for('form_result'))

    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


# Helpers

def save_data(string):
    
    if not 'dane' in os.listdir():
        os.mkdir('dane')
        if not 'notatnik.txt' in os.listdir('dane'):
             os.system('touch notatnik.txt')
            
    with open('dane/notatnik.txt', "a+") as f:
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
            ('a','b'),
            ('c','c'),
            ('d','d'),
    ]

    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('kk')

class Y(FlaskForm):
    y_options = [
            ('rock','rock'),
            ('pop','pop'),
            ('rap','rap'),
            ('metal','metal'),
    ]

    music = StringField('Ulubiony utwór - link:', validators=[DataRequired()])
    my_music_state = SelectField('Ulubiona muzyka:', choices=y_options)
    follow_me = BooleanField('Subskrybuj mnie na youtube :)')

    button = SubmitField('ok')


#####################################################################################
if __name__=="__main__":
    app.run()
