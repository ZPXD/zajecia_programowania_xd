from flask import Flask, render_template, redirect, url_for

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os


app = Flask(__name__)

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

@app.route('/form_b')
def form_b():
    form = Bb()
    if form.validate_on_submit():
        y_name = form.y_name.data
        y_age = form.y_age.data
        fav_music = form.fav_music.data

        string = '{} w wieku {} lubi ,,{}".\n'.format(y_name, y_age, fav_music)
        save_dataB(string)

        return redirect( url_for('form_result'))

    return render_template("form_b.html", form=form)

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


# Helpers

def save_data(string):
    with open('data/data.txt', "a") as f:
        f.write(string)

def save_dataB(string):
    if not 'dane' in os.listdir():
        os.mkdir('dane')
        if not 'formularz.txt' in os.listdir('dane'):
             os.system('touch formularz.txt')
            
    with open('dane/formularz.txt', "a+") as f: #dodatnie czegoś nowego do pliku to a+
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


class Bb(FlaskForm):
    age_options = [
        ('niepelnoletni', '<18'),
        ('pelnoletni, mlodzi', '18-30'),
        ('dorosli', '>30'),
    ]

    y_name = StringField('Podaj swoje imie:', validators = [DataRequired()])
    y_age = SelectField('Jestem w wieku:', choices = age_options)
    fav_music = StringField('Podaj tytul swojej ulubionej książki:', validators=[DataRequired()])

    button = SubmitField('Wyslij')




if __name__=="__main__":
    app.run(debug=True)
