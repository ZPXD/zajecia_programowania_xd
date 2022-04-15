### II. Pobierz i uruchom projekt
#### (git clone, środowisko, biblioteki i uruchomienie projektu)

TL;DR: jak powyższe gra, to poznaj [url_repozytorium](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/url_repozytorium.md), skopiuj je i uruchom korzystając z poniższego kodu:
```
repo_url=tu_wklej_url
```
I wklej wszystkie poniższe linie:
```
git clone $repo_url
srodowisko="${PWD##*/}env"
srodowisko=${srodowisko%.*}_${srodowisko##*.}
python3 -m venv $srodowisko
source $srodowisko/bin/activate
pip3 install -r requirements.txt
```
i jeżeli projekt ma formę strony www:
```
export FLASK_APP=app.py
flask run
```
Po odpaleniu aplikacji wejdź na http://127.0.0.1:5000/ 

a jeżeli projekt ma formę skryptu (sprawdzisz skrypty w folderze wpisując `ls`):
```
python3 nazwa_skryptu.py
```

## Dokładniejszy opis:

#### 1. Pobierz repozytorium:

1. Wejdź na stornę główną repozytorium projektu - np. `https://github.com/ZPXD/arena.xd`.
2. Znajdź zielony przycisk `code`
3. Skopiuj url `https://github.com/ZPXD/arena.xd.git`
4. Uruchom poniższą komendę zamieniając `repo_url` na skopiowany w poprzednim kroku url projektu
```
git clone repo_url
```

#### 2. Uruchom środowisko i zainstaluj biblioteki:

Pierwsze dwie linie przypisują do zmiennej nazwę środowiska a ostatnie dwie je tworzą i aktywują.

```
srodowisko="${PWD##*/}env"
srodowisko=${srodowisko%.*}_${srodowisko##*.}
python3 -m venv $srodowisko
source $srodowisko/bin/activate
```
Środowisko projektu będzie zawsze miało nazwę folderu repozytorium + "env" z "_" zamiast kropek.

Aby wyjść ze środowiska, wpisz:
```
deactivate
```

#### Zainstaluj wymagane biblioteki:
Dalej będąc w środowisku (!) wpisz:
```
pip3 install -r requirements.txt
```

#### 3. Uruchom program:

A. Projekt w formie  **strony www**
```
export FLASK_APP=app.py
flask run
```

Po odpaleniu aplikacji wejdź na http://127.0.0.1:5000/


B. Projekt **w formie skryptu** - (sprawdzisz skrypty w folderze wpisując `ls`):
```
python3 nazwa_skryptu.py
```
