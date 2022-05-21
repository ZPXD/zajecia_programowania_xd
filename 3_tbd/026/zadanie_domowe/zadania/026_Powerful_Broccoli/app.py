from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from moje_programy.form_music import X
from moje_programy.form_music import save_data
from moje_programy.muzyka import read_music
from moje_programy.yt import get_yt_link

###############################
#Nie wiem czy ten kod będzie działał bo go kopiowałem z flagi
#Tu można zobaczyć jak wygląda stronna
# https://maksprojekt.pl/muzyka
# https://maksprojekt.pl/form_music
###############################

app=Flask(__name__)

app.secret_key = 'gus'

@app.route('/')
def index():
    text = "https://maksprojekt.pl/muzyka"
    return render_template("index.html", text=text)

@app.route('/form_music', methods=["GET", "POST"])
def form():
    form = X()

    if form.validate_on_submit():        
        wykonawca = form.wykonawca.data
        utwor = form.utwor.data
        date = datetime.now(tz=None).strftime("%Y-%m-%d %H:%M:%S")
        kto = form.kto.data
        link = get_yt_link(wykonawca,utwor)
        string= f'"{wykonawca.strip()}","{utwor.strip()}",{date},"{kto.strip()}",{link}\n'
        save_data(string)
        return redirect( url_for('muzyka'))

    return render_template("form_music.html", form=form)

@app.route('/muzyka')
def muzyka():
    return render_template("muzyka.html", lst = read_music())

if __name__=="__main__":
    app.run(debug=True)