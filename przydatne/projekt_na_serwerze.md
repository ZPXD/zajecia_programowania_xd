## Uruchom projekt na serwerze z systemem Linux Ubuntu 18/20

Kroki:
1. Przygotowanie po Twojej stronie (komputer, wymagania, użytkownik, folder)
2. Pobierz i uruchom projekt
3. Nauka
4. Kontrybucja

#### I. Przygotowanie po Twojej stronie:
#### (serwer, użytkownik, zainstalowane: python3, pip3, venv, git i otwórz terminal, wejdź w miejsce na projekt).

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

#### A. na serwerze jeżeli projekt ma formę strony www:
```
export FLASK_APP=app.py
flask run
```

Normalnie rezultat był by widziany w przeglądarce. Jednak jako, że pracuejsz na serwerze, to: otwórz jeszcze jeden nowy terminal lub powershell będąc na swoim komputerze i wpisz:

za username -  wstaw nazwę użytkownika
za klucz - nazwę pliku klucza lub ścieżkę do klucza
za 1.1.1.1 – ip serwera
```
ssh -L 5000:localhost:80 -i klucz username@1.1.1.1
```

Po odpaleniu aplikacji wejdź na http://127.0.0.1:5000/ u siebie na komputerze: teraz zadziała.


#### B. Na serwerze jeżeli projekt ma formę skryptu (sprawdzisz skrypty w folderze wpisując `ls`):
```
python3 nazwa_skryptu.py
```

#### III. Nauka

TBC. TL;DR: poczytaj kod, poucz się.

#### IV. Kontrybucja i rozwój

TBC.

Aby dołączyć do rozwoju, przeczytaj pracy z git, o pracy z branchami i PR.

```
link_repo=None
nazwa_branchu=main
git -b $nazwa_branchu $link_repo
```

