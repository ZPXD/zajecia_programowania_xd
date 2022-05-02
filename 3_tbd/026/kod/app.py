from flask import Flask, render_template, redirect, url_for

import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = ':)'


# Main

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form_a', methods=["GET", "POST"])
def form_a():
    form = X()
    if form.validate_on_submit():
        x = form.x.data
        y = form.y.data
        z = form.z.data
        string = '{}\n{}\n{}\n\n'.format(x, y, z)
        save_data(string)
        return redirect( url_for('index'))
    return render_template("form_a.html", form=form)

@app.route('/form_b')
def form_b():
    return render_template("form_b.html")

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
            ('b','b'),
            ('c','c'),
    ]
    x = StringField('x', validators=[DataRequired()])
    y = SelectField('y', choices=x_options)
    z = BooleanField('z')
    button = SubmitField('kk')


if __name__=="__main__":
    app.run(debug=True)

