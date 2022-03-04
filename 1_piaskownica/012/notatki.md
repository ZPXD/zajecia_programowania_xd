012 - Python

--------------------------------------------------------------------------------

Sygnatury czasowe filmu na YT:

YT: https://www.youtube.com/watch?v=P3pi3Co1wDI



0:33 - co słychać teraz i zapowiedź tego, co będzie się działo  
9:00 - prezentacja filmiku „Etap 7 - Hiper ASAP - od gołego serwera do flagi w 15 minut”  
15:02 - koniec wprowadzenia do zajęć nr 12  
15:34 - określenie narzędzi potrzebych na dzisiejszą lekcję (discord, Github: repozytoria ZPXD i własne)  
17:00 - krótkie wprowadzenie do minimalnych umiejętności obsługi Git-a  
22:45 - Jak forkować (wprowadzać „swoje” odgałęzienie czyjegoś projektu)  
24:30 - Github - wprowadzenie (git clone)  
26:30 - wprowadzanie zmian na dysku lokalnym i synchronizowanie zmian z githubem (git pull -> czyli aktualizacja z serwera Github)  
29:20 - Obsługa git z Visual Studio Code  
30:30 - git clone z terminala VSC  
32:40 - git clone w VSC kliknięciami myszy  
35:24 - komendy terminala VSC do usunięcia repozytorium git (usunięcie folderu: _sudo rm -r cwiecznia-git_)  
37:03 - jak usunąć problem z klonowaniem repozytorium przez VSC (aż do 41:55) - otwieranie w nowym oknie VSC)  
42:05 - dobrą praktyką jest otwieranie nowego okna VSC dla nowego połączenia lub nowego folderu  
43:30 - git fork - omówienie na przykładzie Github-a  
44:20 - czym jest fork? Widelcowaniem :) Czyli stworzeniem własnego odgałęzienia czyjegoś projektu  
45:40 - fetch upstream - pobieranie zmian wprowadzonych w repozytorium głównym do własnego forka  
48:45 - ponowna prezentacja procedury „fetch upstream”  
51:40 - przykład dla usuniętego pliku  
52:30 - ponowne „fetch upstream” i „fetch and merge”  
54:30 - ponowne forkowanie (innego repozytorium)  
55:20 - pytanie: „jestem ahead” ;) - co robić? jak żyć? ;)  
57:00 - przykład: kopiowanie folderu lokalnego do innej lokalizacji (z linii komend terminala)  
1:00:12 - ćwiczenia git-a ciąg dalszy (level 1)  
1:00:50 - tworzenie własnego repozytorium na Githubie  
1:02:00 - nadawanie nazwy własnemu repozytorium - różne style nazewnictwa  
1:04:10 - dodawanie opisu (deskrypcji) repozytorium; ustawianie rodzaju (prywatne/publiczne), licencji i opisu w pliku README  
1:10:45 - poruszenie tematu pustego repozytorium i problemów z nim związanych  
1:13:15 - poruszanie się po własnym repozytorium w serwisie Github  
1:13:55 - co możemy zrobić z własnym repozytorium? Wysyłamy link do własnego repo :)  
1:15:00 - dodawanie plików do własnego repozytorium i ich edycja bezpośrednio w serwisie Github  
1:16:19 - VSC a Github  
1:17:00 - klonowanie własnego repozytorium na serwer za pomocą VSC  
1:19:00 - synchronizowanie zmian wykonanych w plikach edytowanych w VSC z repozytorium na Github  
1:21:00 - klikany „git stage” i „git commit” w VSC, a następnie „git push” i jego konfiguracja  
1:24:00 - „git config --global user.name "TWOJA NAZWA UŻYTKOWNIKA GITHUB-a"” i „git config --global user.email "TWOJA NAZWA KONTA E-MAIL UŻYTKOWNIKA GITHUB-a"”  
1:26:00 - ponowna prezentacja synchronizacji zmian w plikach z repozytorium na Github  
1:29:05 - instrukcja autoryzacji Github  
1:32:40 - prezentacja w terminalu (czyszczenie, tworzenie katalogu) a następnie jego dołączanie do git-a za pomocą VSC  
1:34:50 - „publish to GitHub” w VSC  
1:35:40 - jak zintegrować Git-a z VSC („authorize github”)  
1:38:42 - Szybkie powtórzenie dwóch ścieżek (1. Tworzenie repo bezpośrednio na githubie oraz 2. Tworzenie repo na VSC)  
1:43:00 - powtórzenie wcześniejszych czynności  
1:44:30 - wyjawienie tajemnicy dalszych losów repozytorium „cwiczenia-git” ;)  
1:46:00 - „Jak wrzucać zmiany ze swojego forka na repo innej osoby” - informacja o przeniesieniu prezentacji „Pull requests” na kolejne zajęcia  
1:48:30 - ćwiczenia z synchronizacji (wraz z sakramentalnymi słowami kol. Botula: „zawsze zaczynamy od git pull-a!”)  
1:52:00 - ćwiczenia z usuwania problemów pull/push  
1:54:30 - o tym, dlaczego na razie lepiej nie robić konfliktów git-a ;)  
1:58:40 - stage'owanie zmian w VSC  
2:04:19 - podsumowanie zajęć  
2:05:15 - zapowiedź PR („pull requests”) i zadanie pracy domowej :-D  
2:10:30 - ustawiajcie silne hasła na swoich serwerach, a jeszcze lepiej - włączcie logowanie kluczem, a wyłączcie logowanie hasłem na swoje serwery   



----------------------------------------------------------

### NOTATKA z zajęć

#### 07.03.22 - Start II części zajęć

- każde zajęcia - 1 mała rzecz + PR
- zadanie domowe - zadanie tygodniowe + PR

#### Jak dołączać:

1. Szturm
2. Dla nowych i chętnych: Piaskownica 001-012
3. Systematyzacja + klocki

----------------------------------------------------------

#### Materiał dzisiaj:
 
1. GIT:

- VSCode: clone, fetch, dodanie repo, commit, pull, push, PR
- GitHub:
- Nie będzie: Jak robić to z linii wiersza poleceń: terminala.

2. Napiszemy program do sprawdzania zadań domowych

3. Ogólnie - rzucimy okiem na bardziej rozbudowany kod.
        
    git clone Xxxxxxxxxxxxxxxx  
> na przykład:
>     git clone git@github.com:ZPXD/cwiczenia-git.git

4. Kod z zajęć:

	4.1. Szybkie rozpoczęcie pracy z git-em:

> przechodzimy do katalogu ze świeżo sklonowanym repozytorium

    cd Xxxxxxxxxxxxxxxx         

> robimy jakąś zmianę na dysku (np. tworzymy plik)
 
> Następnie dodajemy zmienione pliki do „poczekalni git-a” („staging area”).

    git add .                   

> Kropka oznacza bieżący katalog roboczy - to oznacza, że do git'a będą dodane wszystkie zmienione pliki  
> z bieżącego katalogu roboczego.


> zatwierdzanie zmian („commit”)
> Inaczej mówiąc jest to wypchnięcie zmienionych plików z „poczekalni” do migawki git-a

    git commit -m "komentarz jakiś"  
                               
> Wypchnięcie zmian do zdalnego repozytorium, np. na Github, lub na własny zdalny serwer.

    git push                    

4.2. Dalsza praca z git-em

    git pull                            
    dodaj/usun coś                      
    git add .                           
    git commit -m "komentarz jakiś"     
    git push                            
