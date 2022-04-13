## Uruchom projekt u siebie na komputerze z systemem Linux Ubuntu 18/20

#### Kroki:

Przygotowanie:
1. Jeżeli nie masz serwera, zdobądź go i przygotuj.
2. Zainstaluj wymagane oprogramowanie
3. Miejsce na projekt
4. Użytkownik

Projekt:
5. Pobierz
6. Przygotuj środowisko projektu i biblioteki
7. Uruchom

#### 1. Przygotowanie wymaganego oprogramowania:

Potrzebujesz na serwerze Linuxie Ubuntu co następuje: 
1. python3
2. pip3 
3. venv

Jeżeli czegoś Ci brakuje, uruchom skrypt `server_preparation_for_project.sh` wpisując:
```
wget -q 'https://raw.githubusercontent.com/ZPXD/zajecia_programowania_xd/main/przydatne/server_preparation_for_project.sh' && chmod +x server_preparation_for_project.sh && ./server_preparation_for_project.sh;
```
Lub uruchom poniższe polecenia:
```
apt update
apt install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools --yes
apt install python3-pip
pip3 install virtualenv
```

Upewnij się, że jesteś zalogowany jako użytkownik w folderze w którym chcesz zapisać projekt. 

#### 2. Użytkownik

Zaloguj się na swojego użytkownika na serwerze lub na swoim komputerze. Wstaw pod `nazwa_uzytkownika` nazwę jaką masz na serwerze lub na swoim komputerze.
```
su nazwa_uzytkownika
```

#### 3. Miejsce

Na serwerze zajęciowym dobry folder na projekty które są uruchamiane także w formie www to `/var/www`. Wejdziesz tam wpisując w terminalu:
```
cd /var/www
``` 
lub jeżeli nie będą uruchamiane jako serwisy www, możesz założyć nowy folder w tym celu:
```
cd /home/$USER
mkdir projekty_zpxd
cd projekty_zpxd
```

Na własnym komputerze projekty proponuje także trzymać w 1 miejscu:
```
cd
mkdir projekty_zpxd
cd projekty_zpxd
```

#### 4. Pobierz:

W poniższy kod wstaw zamiast repo_url link który znajdziesz klikając w zielony przycisk "code" na głównej stronie repozytorium.
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

Jeżeli to aplikacja www:
```
export FLASK_APP=app.py
flask run
```
Jeżeli to skrypt, to zamień w poniższym poleceniu `nazwa_skryptu.py` na nazwę programu i go uruchomisz:
```
python3 nazwa_skryptu.py
```
Aby sprawdzić zawartość plików w folderze, wpisz:
```
ls -la
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
