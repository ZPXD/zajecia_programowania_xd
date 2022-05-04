from flask import Flask, render_template, redirect, url_for

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app=Flask(__name__)
app.secret_key = ':)'


# Strona podstawiwa index

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)




# 2 formularze a i b

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
        
        tytul_utworu = form.tytul_utworu.data
        typ_utworu = form.typ_utworu.data
        inny_typ = form.inny_typ.data
        wszystko_ok = form.wszystko_ok.data

        string = '{}\n{}\n{}\n{}\n\n'.format(tytul_utworu, typ_utworu, inny_typ, wszystko_ok)
        save_data_b(string)

        return redirect( url_for('form_b_result'))

    return render_template("form_b.html", form=form)






# rezultat po wypełnieniu formularza 

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")

@app.route('/form_b_result')
def form_b_result():
    return render_template("form_b_result.html")


# Helpers - zapisywanie danych z formularza do pliku

def save_data(string):
    with open('data/data.txt', "a") as f:
        f.write(string)

def save_data_b(string):
    with open('data/datab.txt', "a") as f:
        f.write(string)


# Errors

@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500


# Form - formularz

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
            ('Wybierz_opcje','Wybierz Opcje'),
            ('Techno','Techno'),
            ('Dance','Dance'),
            ('House','House'),
            ('Disco-Polo','Disco-Polo'),
            ('Rap','Rap'),
            ('Inne','Inne'),
    ]

    tytul_utworu = StringField('Podaj tytuł polecanego utworu:', validators=[DataRequired()])
    typ_utworu = SelectField('Jaki to typ muzyki?:', choices=y_options)
    inny_typ = StringField('Jeśli inny typ to podaj jaki :) :')
    wszystko_ok = BooleanField('Wszystko poprawnie wpisane? :)')
    button = SubmitField('Wyślij')








#towrzenie pod strony
@app.route('/xd')
def xd():
    return render_template("xd.html")
#twozenie konca podstrony


@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga_dla_ukrainy.html")



import random
from moje_programy.character_wiki import character
from moje_programy.open_poem import open_poem
@app.route('/brudnopis')
def brudnopis():
    super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Kopernik', 'Małysz']
    chosen_hero = random.choice( super_heroes)
    description = character( chosen_hero).encode('utf-8').decode()
    poem_lines = open_poem()
    return render_template("brudnopis.html", hero=chosen_hero, description=description, poem_lines=poem_lines)



from moje_programy.character_wiki import character
import random
@app.route('/ciekawe-postacie')
def ciekawe_postacie():
    lista_ciekawych_postaci = [
        'Pudzianowski',         # 0
        'Małysz',               # 1
        'Kopernik',             # 2
        'Maria Skłodowska',     # 3
        'Kościuszko',           # 4
        'Donald',               # 5
        'Myszka Miki',          # 6
        'Putin',                # 7
        'Steve Jobs',           # 8
        'Marek Grechuta',       # 9
        'Andrzej Gołota',       #10
        'Tomasz Chomyszyn',
    ]
    opisy_postaci = []
    for i in range(3):
        postac = random.choice(lista_ciekawych_postaci)
        indeks = lista_ciekawych_postaci.index(postac)
        lista_ciekawych_postaci.pop(indeks)

        opis_postaci = character(postac)
        dlugosc_opisu = len(opis_postaci)
## Podzielenie tekstu na słowa i ich policznie
        podzial_testu = opis_postaci.split (' ')
        ilosc_slow = len(podzial_testu)
## Koniec podziału i licznia słow 
        info = [postac, opis_postaci, dlugosc_opisu, ilosc_slow]
        opisy_postaci.append(info)

    def element_4(lista):
        element = lista[3]
        return element
    opisy_postaci.sort(reverse=True,key=element_4)

    return render_template("ciekawe-postacie.html", opisy_postaci=opisy_postaci)






#uruchamia aplikacje
if __name__=="__main__":
    app.run()

