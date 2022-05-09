## Python - środowisko

[Dokumentacja](https://docs.python.org/3/library/venv.html)

Środowisko min. pozwala na gromadzenie zmiennych środowiskowych i bibliotek Pythona dedykowanych dla Tego projektu.


#### Stwórz i włącz środowisko:

O nazwie folderu w jakim jesteś:
```
venv_name=${PWD##*/}
venv_name+=venv
python3 -m venv $venv_name
source $venv_name/bin/activate
```

Lub sam zdefiniuj nazwę:
```
python3 -m venv <nazwa_srodowiska>      # Tworzy środowisko
source <nazwa_srodowiska>/bin/activate  # Aktywuje środowisko
```

#### Wyłącz środowisko
```
deactivate
```

#### Wylistuj wszystkie zmienne środowiskowe
```
env
```

#### Przyspieszenie:

Wylistuj biblioteki wewnątrz środowiska.
```
pip3 freeze
```

Zapisz wszystkie biblioteki zainstalowane w środowisku do pliku `requirements.txt`.
```
pip3 freeze > requirements.txt
```

Instalacja biblioteki przez `pip3`.
```
pip3 install <nazwa-biblioteki>
```
