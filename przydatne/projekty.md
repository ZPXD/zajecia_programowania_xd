

# Projekty

Jeżeli w pliku README.md projektu nie jest opisane inaczej, wykonaj następujące kroki aby uczyć się lub dołączyć do kontrybucji.

1. Pobieranie
2. Środowisko
3. Biblioteki
4. Uruchomienie
 
## Jak uruchomić:

Będąc na przygotowanym serwerze albo u siebie na przygotowanym komputerze (przygotowanym czyli masz git, python3, pip3, venv, ssh).

Upewnij się, że jesteś zalogowany jako użytkownik w folderze w którym chcesz zapisać projekt. 

#### 1. Użytkownik

Zaloguj się na swojego użytkownika na serwerze lub na swoim komputerze. Wstaw pod `nazwa_uzytkownika` nazwę jaką masz na serwerze lub na swoim komputerze.
```
su nazwa_uzytkownika
```

#### 2. Miejsce

Jeżeli jesteś u siebie na komputerze, to może być:
```
cd
mkdir projekty_zpxd
cd projekty_zpxd
```
Jeżeli jesteś na serwerze zajęciowym, spróbuj:
```
cd /var/www
``` 
lub
```
cd /home/$USER
```

#### 3 Pobierz:

W poniższy kod wstaw zamiast repo_url link który znajdziesz klikając w zielony przycisk "code" na głównej stronie repozytorium.
```
repo_url=None
git clone $repo_url
```

#### 4. Uruchom środowisko:

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

#### 5. Zainstaluj wymagane biblioteki:
```
pip3 install -r requirements.txt
```

#### 6. Uruchom program:

```
export FLASK_APP=app.py
flask run
```

#### Oglądaj rezultaty w przeglądarce

#### A: na własnym kompie:

Po odpaleniu aplikacji wejdź na http://127.0.0.1:5000/

#### B: na serwerze:

Otwórz nowy terminal lub powershell będąc na swoim komputerze i wpisz:

za username -  wstaw nazwę użytkownika
za klucz - nazwę pliku klucza lub ścieżkę do klucza
za 1.1.1.1 – ip serwera
```
ssh -L 5000:localhost:80 -i kluc username@1.1.1.1
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
