## Jak uruchomić projekt?

Każdy projekt ma swoją instrukcję. Jeżeli jej nie ma a linkuje tutaj, to znaczy, że wystarczą opisane niżej standardowe kroki aby projekt uruchomić i do niego dołączyć. 

Zobacz niżej która droga odpowiada Twoim celom i wykonaj opisane tam kroki aby uczyć się lub dołączyć do kontrybucji.

1. Pobieranie
2. Środowisko
3. Biblioteki
4. Uruchomienie


#### Jak uruchomić projekt u siebie, pouczyć się i dołączyć do kontrybucji?

1. Na serwerze zajęciowym (Linux Ubuntu 18/20) [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/projekt_na_serwerze.md)
2. U siebie na komputerze (Linux Ubuntu 18/20) [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/projekt_na_komputerze_linux_ubuntu.md)
3. U siebie na komputerze (Windows 10/11) [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/projekt_na_komputerze_windows.md)
4. U siebie na komputerze (MAC OS) [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/projekt_na_komputerze_mac_os.md)


## Jak uruchomić:

Będąc na przygotowanym serwerze albo u siebie na przygotowanym komputerze (przygotowanym czyli masz git, python3, pip3, venv, ssh).

Upewnij się, że jesteś zalogowany jako użytkownik w folderze w którym chcesz zapisać projekt. 

#### 1. Użytkownik

Zaloguj się na swojego użytkownika na serwerze lub na swoim komputerze. Wstaw pod `nazwa_uzytkownika` nazwę jaką masz na serwerze lub na swoim komputerze.
```
su nazwa_uzytkownika
```

#### 2. Miejsce

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
