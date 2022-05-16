from flask import Flask, render_template, redirect, url_for
import os, random, flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.secret_key = ':)'

# Main

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

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
    form_h = Holidays()

    if form_h.validate_on_submit():
        holiday_spot = form_h.holiday_spot.data
        holiday_preferences = form_h.holiday_preferences_categorical.data
        holiday_question = form_h.holiday_question.data

        holiday_data = '{}\n{}\n{}\n\n'.format(holiday_spot, holiday_preferences, holiday_question)
        save_data(holiday_data)

        return redirect(url_for('form_result'))
    return render_template("form_b.html", form_h=form_h)
    
@app.route('/form_result')
def form_result():
    return render_template("form_result.html")


# Helpers

def save_data(string):
    with open('dane/data.txt', "a") as f:
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
            ('a_1','a_2'),
            ('b_1','b_2'),
            ('c_1','c_2'),
            ('d_1','d_2'),
    ]

    github = StringField('Twój github:', validators=[DataRequired()])
    my_github_state = SelectField('Ogarniam githuba na:', choices=x_options)
    follow_me = BooleanField('Followuj mnie na gitubie :)')

    button = SubmitField('Ok!')

class Holidays(FlaskForm):
    holidays_preferences_options = [
        ('opt_mountains', "Gory"),
        ('opt_sea', "Morze"),
        ('opt_lake', "Jezioro"),
        ('opt_other', "Inne")
    ]

    holiday_spot = StringField("Polecana destynacja wakacyjna dla rodziny z dziecmi:",
                    validators = [DataRequired()])
    holiday_preferences_categorical = SelectField("Twoje preferowane miejsce wakacji:",
                    choices = holidays_preferences_options)
    holiday_question = BooleanField('Czy lubisz jezdzic z dziecmi na wakacje?')

    holiday_button = SubmitField("Wyslij odpowiedzi")

if __name__=="__main__":
    app.run(debug=True)
