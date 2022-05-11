from flask import Flask, render_template, redirect, url_for

import os
import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.secret_key = ':)'

#strona glowna 
@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

#podstrona xd
@app.route('/xd')
def xd():
    return render_template("xd.html")


#2 formularz na stronce www + rezultat
@app.route('/form_a', methods=["GET", "POST"])
def form_a():

    form = X() # odwolanie do klasy ktora znajduje sie ponizej i tworzy formularz
    if form.validate_on_submit(): # jeżeli sie nie kliknie submita to nie bedzie true i if sie nie wydarzy

        github = form.github.data # wyciagniecie z pola formularza i przypisanie odp do zmiennej
        my_github_state = form.my_github_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(github, my_github_state, follow_me) # z trzech odp tworzy stringa 
        save_data(string)# i zapisuje w > funkcja w helpers
        
        return redirect( url_for('form_result'))# jezeli if sie spelni przenosi na ta strone
    return render_template("form_a.html", form=form) # jezeli sie nie wykona if to 'odswieza' sie strona

@app.route('/form_b', methods=["GET","POST"])
def form_b():
    form = Y()
    if form.validate_on_submit():
        love_caffe = form.love_caffe.data
        milk = form.milk.data
        kind_caffe = form.kind_caffe.data
        str_caffe = '{}\n{}\n{}\n\n'.format(love_caffe,milk,kind_caffe)
        save_info(str_caffe)
        return redirect( url_for('form_result'))

    return render_template('form_b.html', form = form)

@app.route('/form_result')
def form_result():
    return render_template('form_result.html')

# Helpers
def save_data(string):

    if not 'dane' in os.listdir():
        os.mkdir('dane')
        if not 'notatnik.txt' in os.listdir('dane'):
            os.system('touch notatnik.txt')
    with open("dane/notatnik.txt", 'a+') as f:
        f.write(string)

def save_info(str_caffe):
    if not 'dane' in os.listdir():
        os.mkdir('dane')
        if not 'notatnik_caffe.txt' in os.listdir('dane'):
            os.system('touch notatnik_caffe.txt')
    with open('dane/notatnik_caffe.txt', 'a+') as f:
        f.write(str_caffe)

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
        ('a','a'), # pierwsze jak chcesz cos nazwac a drugie jak chcesz zeby zostalo to wyswitlone
        ('b','b'),
        ('c','c'),
        ('d','d'),
    ]

    github = StringField('Twoj github:', validators=[DataRequired()]) # validator sprawdza czy pole zostalo wypelnione
    my_github_state = SelectField('Ogarniam githuba na:', choices= x_options) #pierwsze w nawiasie to to co wyswietla sie na stronie przy okienku ankiety
    follow_me = BooleanField('Follow me on github!')

    button = SubmitField('Wyślij')

class Y(FlaskForm):
    y_options = [
        ('lactose free','lactose free'), 
        ('cow milk','cow milk'),
        ('oat milk','oat milk'),
        ('almond milk','almond milk'),
    ]
    love_caffe = BooleanField('Do you like caffe?')
    milk = SelectField('Kind of milk:', choices= y_options) 
    kind_caffe = StringField('Favorite type of coffee', validators=[DataRequired()]) 

    button = SubmitField('Potwierdź')

if __name__=="__main__":
    app.run(debug=True)
