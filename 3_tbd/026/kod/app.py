from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired # Length, ValidationError


app = Flask(__name__)

app.secret_key = ':)'


# Main

@app.route('/')
def index():
    return render_template("index.html")


# Forms
@app.route('/form_a', methods=["GET", "POST"])
def form_a():
    form = A()
    if form.validate_on_submit():
        github = form.github.data
        my_github_state = form.my_github_state.data
        follow_me = form.follow_me.data

        string = '{}\n{}\n{}\n\n'.format(github, my_github_state, follow_me)
        save_data(string)

        return redirect(url_for('form_result'))

    return render_template("form_a.html", form=form)


@app.route('/form_b', methods=["GET", "POST"])
def form_b():
    form = B()
    if form.validate_on_submit():
        your_name = form.your_name.data
        gender = form.gender.data
        no_choice = form.no_choice.data
        
        string = '\n\n\n\n'.format(your_name, gender, no_choice)
        save_data(string)
        
        return redirect(url_for('form_result'))
        
    return render_template("form_b.html", form=form)


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

class A(FlaskForm):
    x_options = [
        ('a', 'a'),
        ('a', 'b'),
        ('c', 'c'),
        ('d', 'd'),
    ]
    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('kk')

class B(FlaskForm):
    y_options = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = SelectField("Wybierz płeć:", choices=y_options)
    your_name = StringField("Twoje imię:", validators=[DataRequired()])
    no_choice = BooleanField("Poziom zadowolenia z zajęć: Zaznacz dla 10/10 odznacz dla 11/10... xD")
    
    button = SubmitField('xD')
    
    
if __name__ == "__main__":
    app.run(debug=True)
