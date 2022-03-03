git clone Xxxxxxxxxxxxxxxx  # na przykład:
                            #  git clone git@github.com:ZPXD/cwiczenia-git.git

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
                            # (np. na Github, lub na własny zdalny serwer)
