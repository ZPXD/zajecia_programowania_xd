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
python3 -m venv <nazwa_srodowiska>
source <nazwa_srodowiska>/bin/activate
```
#### Wyłącz środowisko
```
deactivate
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


```
pip3 install <nazwa-biblioteki>
```
