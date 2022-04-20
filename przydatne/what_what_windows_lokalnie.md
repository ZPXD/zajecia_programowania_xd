##Windows:

U siebie na kompie potrzebujesz git, Git Bash, python, pip, venv, ssh)
W VSC otwórz nowy terminal (powershell)

###Utwórz nowy folder do projektu i pobierz:

```
mkdir whatwhat
cd whatwhat
git clone https://github.com/ZPXD/what_what.git/
```
#### Utwórz i uruchom środowisko:
```
py -3 -m venv flagaenv
flagaenv\Scripts\activate
```

#### Zainstaluj wymagane biblioteki:
```
cd what_what
pip install -r requirements.txt
```

#### Uruchom program:

```
$env:FLASK_APP = "app" #nie trzeba jeśli aplikacja nazywa sie app.py
flask run
```

### Uruchom program w trybie debugowania:

```
$env:FLASK_ENV = "development"
flask run
```
wejdź na http://127.0.0.1:5000/
