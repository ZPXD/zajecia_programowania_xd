## Przygotuj swój komputer z systemem Linux Ubuntu 18/20 na projekty

### I. Przygotowanie po Twojej stronie:
1. **Internet, komputer i system Linux Ubuntu 18/20** - jeżeli masz, to idź dalej
2. **Programy wymagane wstępnie** - Zainstaluj wymagane oprogramowanie [Instrukcja](https://github.com/ZPXD/zajecia_programowania_xd/blob/main/przydatne/przygotuj_linuxa_na_projekt.sh)
3. **Użytkownik** - Bądź zalogowany jako właściwy użytkownik (opis niżej)
4. **Miejsce** - Wejdź na serwerze do miejsca na projekt (opis niżej)

#### 1. Jeżeli nie masz serwera, zdobądź go i przygotuj.
Jeżeli masz, to idź dalej. Jeżeli nie, to warto ;) w przyszłości będzie tutaj instrukcja jak zainstalować.

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

#### A. Na serwerze:

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
