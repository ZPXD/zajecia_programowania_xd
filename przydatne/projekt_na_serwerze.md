## Uruchom projekt na serwerze zajęciowym z systemem Linux Ubuntu 18/20

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
``
#### Oglądaj rezultaty w przeglądarce

#### B: na serwerze:

Otwórz nowy terminal lub powershell będąc na swoim komputerze i wpisz:

za username -  wstaw nazwę użytkownika
za klucz - nazwę pliku klucza lub ścieżkę do klucza
za 1.1.1.1 – ip serwera
```
ssh -L 5000:localhost:80 -i kluc username@1.1.1.1
```

I wejdź na http://127.0.0.1:5000/
