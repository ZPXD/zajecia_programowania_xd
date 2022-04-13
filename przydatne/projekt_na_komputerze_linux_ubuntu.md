## Uruchom projekt u siebie na komputerze z systemem Linux Ubuntu 18/20

Kroki:

### I. Przygotowanie po Twojej stronie i serwera:
1. **Przygotowany serwer** - Jeżeli nie masz serwera, zdobądź go i przygotuj. O tym jest przygoda: [Szturm na AWS](https://github.com/ZPXD/flaga)
2. **Programy wymagane wstępnie** - Zainstaluj wymagane oprogramowanie [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/przygotuj_linuxa_na_projekt.sh)
3. **Użytkownik** - Bądź zalogowany jako właściwy użytkownik (opis niżej)
4. **Miejsce** - Wejdź na serwerze do miejsca na projekt (opis niżej)

### II. Pobierz i uruchom projekt:
1. **Pobierz** - git clone
2. **Przygotuj** - środowisko i biblioteki
3. **Uruchom** - stronę lub skrypt

W skrócie, jeżeli masz gotowy serwer i jesteś jako właściwy użytkownik we właściwym folderze, ustal url_repo [url_repozytorium](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/url_repozytorium.md):
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
a jeżeli projekt ma formę skryptu:
```
python3 nazwa_skryptu.py
```


## I. Przygotowanie po Twojej stronie i serwera:

#### 1. Jeżeli nie masz serwera, zdobądź go i przygotuj.
Temu dedykowana jest przygoda [Szturm na AWS](https://github.com/ZPXD/flaga).

#### 2. Zainstaluj wymagane oprogramowanie
Potrzebujesz: **git, python3, pip3 i venv**. Jeżeli Szturm na AWS masz za sobą, to masz je zainstalowane. Jeżeli nie, przeczytaj: [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/przygotuj_linuxa_na_projekt.md). lub zainstaluj odpalając poniższy skrypt:
```
wget -q 'https://raw.githubusercontent.com/ZPXD/zajecia_programowania_xd/main/przydatne/server_preparation_for_project.sh' && chmod +x server_preparation_for_project.sh && ./server_preparation_for_project.sh;
```

#### 3. Użytkownik
Zaloguj się na swojego użytkownika na serwerze lub na swoim komputerze. Jeżeli jeszcze nie masz użytkownika na serwerze, stwórz go: [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/linux_uzytkownik.md).
```
su nazwa_uzytkownika
```

#### 4. Miejsce
Jeżeli wiesz gdzie chcesz uruchomić projekt aby działał, przejdź tam. Jeżeli nie:

A. Projekty ze stroną www zakładaj w `/var/www`:
```
cd /var/www
``` 
B. Na projekt w formie skryptów stwórz folder jak nie masz i wejdź do niego:
```
mkdir /home/$USER/projekty_zpxd
cd /home/$USER/projekty_zpxd
```

## II. Pobierz i uruchom projekt:

#### 1. Pobierz repozytorium:

1. Wejdź na stornę główną repozytorium projektu - np. `https://github.com/ZPXD/arena.xd`.
2. Znajdź zielony przycisk `code`
3. Skopiuj url `https://github.com/ZPXD/arena.xd.git`
4. Uruchom poniższą komendę zamieniając `repo_url` na skopiowany w poprzednim kroku url projektu
```
git clone repo_url
```

#### 2. Uruchom środowisko:

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

B. Projekt **w formie skryptu** - zamień w poniższym poleceniu `nazwa_skryptu.py` na nazwę programu i go uruchomisz:
```
python3 nazwa_skryptu.py
```
Aby sprawdzić pliki w repozytorium (w folderze projektu), wpisz:
```
ls -la
```

### Oglądaj rezultaty w przeglądarce

#### A: na własnym kompie:

Po odpaleniu aplikacji wejdź na http://127.0.0.1:5000/

#### B: na serwerze:

Otwórz nowy terminal lub powershell będąc na swoim komputerze i wpisz:

za username -  wstaw nazwę użytkownika
za klucz - nazwę pliku klucza lub ścieżkę do klucza
za 1.1.1.1 – ip serwera
```
ssh -L 5000:localhost:80 -i klucz username@1.1.1.1
```

I wejdź na http://127.0.0.1:5000/

### Co dalej?

#### A. Nauka


#### B. Kontrybucja i rozwój

Aby dołączyć do rozwoju, przeczytaj o pracy z branchami.

```
link_repo=None
nazwa_branchu=main
git -b $nazwa_branchu $link_repo
```



#### Wyjdź ze środowiska
```
deactivate
```
