012 - Python

YT: https://www.youtube.com/watch?v=P3pi3Co1wDI

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




# 07.03.22 - Start II części zajęć
- każde zajęcia - 1 mała rzecz + PR
- zadanie domowe - zadanie tygodniowe + PR

# Jak dołączać:
1. Szturm
2. Dla nowych i chętnych: Piaskownica 001-012
3. Systematyzacja + klocki

----------------------------------------------------------

##### Materiał dzisiaj:
# 
# 1. GIT:
# • VSCode: clone, fetch, dodanie repo, commit, pull, push, PR
# • GitHub:
# • Nie będzie: Jak robić to z linii wiersza poleceń: terminala.

# 2. Napiszemy program do sprawdzania zadań domowych

# 3. Ogólnie - rzucimy okiem na bardziej rozbudowany kod.
git clone Xxxxxxxxxxxxxxxx  # na przykład:
                            #  git clone git@github.com:ZPXD/cwiczenia-git.git

4. Kod z zajęć:
4.1. Szybkie rozpoczęcie pracy z git-em:

cd Xxxxxxxxxxxxxxxx         # przechodzimy do katalogu ze świeżo sklonowanym repozytorium

# dodaj plik/usun plik      # robimy jakąś zmianę na dysku (np. tworzymy plik)

git add .                   # dodajemy do „poczekalni git-a” („staging area”).
                            # Kropka oznacza bieżący katalog roboczy - to oznacza,
                            # że do git'a będą dodane wszystkie zmienione pliki
                            # z bieżącego katalogu roboczego.

git commit -m "komentarz jakiś" # zatwierdzanie zmian („commit”) -
                            # wypchnięcie zmienionych plików z „poczekalni” do
                            # migawki git-a
git push                    # Wypchnięcie zmian do zdalnego repozytorium
                            # (np. na Github, lub na własny zdalny serwer).

4.2. Dalsza praca z git-em

git pull			# 
# dodaj/usun co			#
git add .			# Opis taki jak powyżej.
git commit -m "komentarz jakiś"	#
git push			#
