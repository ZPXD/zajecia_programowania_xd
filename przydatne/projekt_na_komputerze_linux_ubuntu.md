## Uruchom projekt u siebie na komputerze z systemem Linux Ubuntu 18/20

Kroki:
1. Przygotowanie po Twojej stronie (komputer, wymagania, użytkownik, folder)
2. Pobierz i uruchom projekt
3. Nauka
4. Kontrybucja

#### I. Przygotowanie po Twojej stronie:
#### (Komputer, użytkownik, zainstalowane: python3, pip3, venv, git i otwórz terminal, wejdź w miejsce na projekt).

TL;DR: jak masz poinstalowane python3, pip3, venv i git to będąc zalogowany na swojego użytkownika wejdź do folderu przeznaczonego na projekty i ruszaj dalej. Jak coś nie działa to tu jest dokładniejszy opis każdej z kwestii: [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/przygotuj_komputer_z_linuxem_na_projekt.md).

#### II. Pobierz i uruchom projekt:
#### (git clone, środowisko, biblioteki i uruchomienie projektu)

TL;DR: jak powyższe gra, to poznaj [url_repozytorium](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/url_repozytorium.md), skopiuj je i uruchom korzystając z poniższego kodu (jeżeli była by potrzeba, tu jest [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/pobierz_i_uruchom_projekt_linux.md)):
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
### III. Nauka

Odpal projekt, poczytaj kod, poucz się na nim i poznaj jak działa. Dodaj element lub dwa, odejmij, modyfikuj. 

### IV. Kontrybucja i rozwój


Aby dołączyć do rozwoju, przeczytaj pracy z git, o pracy z branchami i PR.

```
link_repo=None
nazwa_branchu=main
git -b $nazwa_branchu $link_repo
```
