## Uruchom projekt u siebie na komputerze z systemem Linux Ubuntu 18/20

#### Kroki:

Przygotowanie:
1. Jeżeli nie masz serwera, zdobądź go i przygotuj [Szturm na AWS](https://github.com/ZPXD/flaga)
2. Zainstaluj wymagane oprogramowanie [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/przygotuj_linuxa_na_projekt.sh)
3. Użytkownik []()
4. Miejsce na projekt []()

Projekt:
5. Pobierz
6. Przygotuj środowisko projektu i biblioteki
7. Uruchom

#### 1. Jeżeli nie masz serwera, zdobądź go i przygotuj


#### 2. Przygotowanie wymaganego oprogramowania

```
wget -q 'https://raw.githubusercontent.com/ZPXD/zajecia_programowania_xd/main/przydatne/server_preparation_for_project.sh' && chmod +x server_preparation_for_project.sh && ./server_preparation_for_project.sh;
```

#### 3. Użytkownik

Zaloguj się na swojego użytkownika na serwerze lub na swoim komputerze. Jeżeli jeszcze nie masz użytkownika na serwerze, stwórz go [Instrukcja]().

```
su nazwa_uzytkownika
```

#### 3. Miejsce

Jeżeli wiesz gdzie chcesz uruchomić projekt i działa, przejdź tam zanim pobierzesz repozytorium. Jeżeli nie wiesz:

#### A. Projekt ze stroną www
Na serwerze zajęciowym dobry folder na projekty które są uruchamiane także w formie www to `/var/www`. Wejdziesz tam wpisując w terminalu:
```
cd /var/www
``` 

#### B. Projekt w formie skryptu

Stwórz folder na projekty, jeżeli jeszcze nie masz i wejdź do niego:
```
mkdir /home/$USER/projekty_zpxd
cd /home/$USER/projekty_zpxd
```

#### 4. Pobierz repozytorium:

W poniższy kod zamiast repo_url wstaw link który znajdziesz klikając w zielony przycisk "code" na głównej stronie repozytorium projektu.
```
repo_url=None
git clone $repo_url
```

#### 5. Uruchom środowisko:

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

#### 6. Zainstaluj wymagane biblioteki:
```
pip3 install -r requirements.txt
```

#### 7. Uruchom program:

#### A. Projekt ze stroną www
```
export FLASK_APP=app.py
flask run
```

#### B. Projekt w formie skryptu

Jeżeli to skrypt, to zamień w poniższym poleceniu `nazwa_skryptu.py` na nazwę programu i go uruchomisz:
```
python3 nazwa_skryptu.py
```
Aby sprawdzić zawartość plików w folderze, wpisz:
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
