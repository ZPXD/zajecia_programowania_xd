from flask import Flask, render_template, redirect, url_for, session
import re

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


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

@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


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
            ('a','b'),
            ('c','c'),
            ('d','d'),
    ]

    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('kk')

#ROZAWIAZANIE

@app.route('/form_b', methods=["GET", "POST"])
def form_b():

    form = X2()
    if form.validate_on_submit():
        session["youtube"] = form.youtube.data

        return redirect( url_for('form_result_youtube'))
    return render_template("form_b.html", form=form)

@app.route('/form_result_youtube')
def form_result_youtube():
    link = session["youtube"]
    save_data(f'{link}\n\n')
    session.pop("youtube")
    link = re.sub(r"watch[?]v=", "embed/", link)
    return render_template("form_result_youtube.html", link=link)

def save_data(string):
    with open('data/data.txt', "a") as f:
        f.write(string)

class X2(FlaskForm):
    youtube = StringField('Twój link do piosenki z yt:', validators=[DataRequired()])
    button = SubmitField('LETS GOO')



if __name__=="__main__":
    app.run(debug=True)
