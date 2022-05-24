from flask import Flask, render_template, request, session, redirect, url_for

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import wtforms.validators

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
@app.route('/form_b', methods = ["GET","POST"])
def form_b():
    form = music_form()
    feedback=""
    # if request.method == 'POST':
    #     return redirect(url_for('form_result'))
    if form.validate_on_submit():
        message=form.mess_box.data
        music_type=form.music_type.data
        # session["message"]=message
        string = '{} - {}\n'.format(music_type, message)
        save_data(string)
        return redirect( url_for('form_result',music_type=music_type))
  
    return render_template("form_b.html",form=form)

@app.route('/form_result')
def form_result():
    # message=session["message"]
    music_type=request.args["music_type"]
    return render_template("form_result.html", music_type=music_type)



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
    
class music_form(FlaskForm):
    m_types=[
        ("Rock", "Rock"),
        ("POP", "POP"),
        ("Heavy metal", "Heavy metal"),
        ("Hip hop", "Hip hop"),
        ("Disco", "Disco")
    ]

    mess_box = StringField('Link do muzyki: ', validators=[wtforms.validators.URL(message="Niepoprawny link!")])
    # mess_box = StringField('Link do muzyki: ', validators=[DataRequired(message="wrong")])
    music_type= SelectField(label="Typ muzyki", choices=m_types)
    button = SubmitField('Wyślij')





if __name__=="__main__":
    app.run(debug=True)
