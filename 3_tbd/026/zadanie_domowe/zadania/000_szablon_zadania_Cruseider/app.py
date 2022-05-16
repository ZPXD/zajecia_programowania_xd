from flask import Flask, render_template, redirect, url_for

# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from moje_programy.postac_wiki import character
#from moje_programy.open_poem import open_poem
import random


app=Flask(__name__)

#----------------------------------------------
app.secret_key = ':)'


# Main

@app.route('/')
def index():
    return render_template("index.html")




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

@app.route('/form_b', methods=["GET", "POST"])
def form_b():

    form = Y()
    if form.validate_on_submit():

        music = form.music.data
        music2 = form.music2.data
        follow_me_music = form.follow_me_music.data

        string = '{}\n{}\n{}\n\n'.format(music, music2, follow_me_music)
        save_data(string)

        return redirect( url_for('form_result'))

    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


# Helpers  #obczaić czy to jest ok !! 

def save_data(string):
    print(string)
    with open('data/data.txt', "a+") as f:   #"a" jest od append 
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
            ('a','1'),
            ('a','5'),
            ('c','10'),
            ('d','100'),
    ]

    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie - https://github.com/Cruseider1 :)')

    button = SubmitField('zapisz i wyślij')

class Y(FlaskForm):

    music = StringField('Podaj tytuł pierwszej piosenki:', validators=[DataRequired()])
    music2 = StringField('Podaj tytuł drugiej piosenki:', validators=[DataRequired()])
    follow_me_music = BooleanField('Followuj mnie na YT - Meridzuana')

    button = SubmitField('zapisz i wyślij')

#----------------------------------------------


@app.route('/Ukraina')
def Ukraina():
    return render_template("Ukraina.html")

#----------------------------------------------

@app.route('/Brudnopis')
def Brudnopis():
    character_list =[
        'Mieszko I',
        'Alan Turing',
        'Iron Man',
        'Nash',
        'Marek Aureliusz'
    ] #lista postaci jaka ma się wyświetlać na stronie randomowo
    character_list2 = [] #tu na czysto będą lądować wyniki kodu poniżej

    for i in range(5):
        interesting_character = random.choice(character_list) # zmienna która ma wybierać konkretną postać
        character_indeks = character_list.index(interesting_character) 
        character_list.pop(character_indeks) #robimy indeksowanie i potem popa żeby postaci się nie powtarzały 

        character_desc = character(interesting_character) #tu załącza się kod z osobnego pliku funkcja /character

        word_list = character_desc.split(' ') #dzieli wyrazy do późniejszego podliczenia
        word_list_len = len(word_list)

        content = [interesting_character, character_desc, word_list_len]
        character_list2.append(content)

    def my_func (e):
        return e[2]

    character_list2.sort(reverse=True,key=my_func)

    return render_template("Brudnopis.html", hero=character_list2) #poem_lines=poem_lines #hero=hero jakby przekazuje z pythona do htmla informacje
#----------------------------------------------

from moje_programy.Generator import losowe
from moje_programy.Generator import losowe2

@app.route('/Generator')
def Generator():
    haslo = losowe()
    haslo2 = losowe2()

    return render_template("Generator.html", haslo=haslo, haslo2=haslo2)

#----------------------------------------------

if __name__=="__main__":
    app.run()
