from flask import Flask, render_template, redirect, url_for, request

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL
import validators

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


@app.route('/form_b', methods=["GET", "POST"])
def form_b():
    form_zad_dom = FormZD()
    form_input_url = ''
    form_checkbox = ''
    url_not_valid = ''
    if request.method == "POST":
        form_input_url = form_zad_dom.form_input_url.data
        if validators.url(form_input_url):
            form_checkbox =  form_zad_dom.form_checkbox.data
            if form_checkbox:
                string_save_in_file = '{}\n{}\n\n'.format(form_input_url,form_checkbox)
                save_data(string_save_in_file)

            return redirect( url_for('form_result_fuction',form_checkbox=form_checkbox))
        else:
            url_not_valid = 1
    
    return render_template("form_b.html", form_zad_dom=form_zad_dom, url_not_valid=url_not_valid)

@app.route('/form_result_fuction', methods=["GET", "POST"])
def form_result_fuction():
    if request.args.get('form_checkbox') == 'True':
        return "Twoja strona została dodana, <a href="+url_for('form_b')+">wróć do poprzedniej strony</a>"
    else:
        return "Twoja strona nie została dodana, <a href="+url_for('form_b')+">wróć do poprzedniej strony</a>"
        


# Helpers
def save_data(string):
    with open('data/data_zad_dom.txt', "a") as f:
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

class FormZD(FlaskForm):
    form_input_url = StringField('Wpisz ciekawy adres url', validators=[DataRequired(), URL(message='Nieprawidłowy adres url')])
    form_checkbox = BooleanField('Zapisz link w pliku')

    form_submit = SubmitField('Wykonaj')



if __name__=="__main__":
    app.run(debug=True)
