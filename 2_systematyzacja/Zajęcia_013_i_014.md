#### Flaga dla Ukrainy


#### Kod w pliku app.py (/var/www/flaga/app.py)

Wklej w pliku app.py:
```
@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("flaga-dla-ukrainy.html")
```

I dodaj plik flaga-dla-ukrainy.html do folderu z plikami html w  folderze templates )w /var/www/flaga/templates/flaga-dla-ukrainy.html)
```
<!DOCTYPE>
<html>
<head>
</head>

<body>
    <br>
    <br>
    <br>
    <br>
    <br>
    <h1 style="text-align:center">xDDD Coś od siebie : )</h1>
</body>

</html>
```


#### Kilka słów od siebie
```
<h1 style="text-align:center">Dużo miłości i siły wam.</h1>
```

#### Flaga Ukrainy (jak dodać do strony www zdjęcie?)

Dodaj na stronę zdjęcie z flagą Ukrainy. Aby to zrobić dodaj do swojej strony (jej pliku html) poniższą linię:
```
<div style="display: flex; justify-content: center"><img src="https://us.edu.pl/wp-content/uploads/obrazek-wyr%C3%B3%C5%BCniaj%C4%85cy/US_obrazek_pomoc_ukraina.png" alt="flag"></div>
```
Jeżeli chcesz, możesz modyfikować fragment **<img src=** - jak się przyjrzysz, zobaczysz, że każdy zapis ma sens, np. tu definiujesz link "url" strony www z obrazkiem. Ten obrazek będzie wyświetlany na stronie z powyższą linią. Dodaj poniższą linię z flagą Polską:                                            
```
<div style="display: flex; justify-content: center"><img src="https://www.wykop.pl/cdn/c3201142/comment_KieFARtNuQivpmwsf27V3vSg6wmzdWBt.jpg" alt="flag"></div>
```


#### Dodaj wsparcia, wyślij kawałek z muzyką (jak dodać do html'a film z YT albo muzykę?):

W htmlu wszystko opiera się na parametrach wewnątrz dziubkowatych nawiasów. W miejsce linku wrzuć muzykę którą chciał byś puścić przyjaciółom z Ukrainy.
```
<div style="display: flex; justify-content: center"></div><iframe width="1309" height="489" src="https://www.youtube.com/embed/y7R1VqpwumE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
```

#### Dodaj inne elementy:

Np.

```
    <h1 style="text-align:center"><div><span style="color: #001eff"></span></div>
        <div><span style="color: #2a44d5">██╗░░██╗██████╗░██████╗░██████╗░</span></div>
        <div><span style="color: #2a44d5ad">╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗</span></div>
        <div><span style="color: #2a44d570">░╚███╔╝░██║░░██║██║░░██║██║░░██║</span></div>
        <div><span style="color: #fbff0070">░██╔██╗░██║░░██║██║░░██║██║░░██║</span></div>
        <div><span style="color: #fbff00ad">██╔╝╚██╗██████╔╝██████╔╝██████╔╝</span></div>
        <div><span style="color: #fbff00">╚═╝░░╚═╝╚═════╝░╚═════╝░╚═════╝░</span></div>
    </h1>
```

Albo:



#### Flavicon

Jak mozna zauważyć, na górze każej zakładki w przeglądarce jest mały obrazek - możesz zmienić jego zawartość w 4 krokach:

1. Stwórz ikonkę 16x16 pikseli z rozszerzeniem .ico. Na przykład na stronie https://www.favicon-generator.org/

2. Zapisz jako favicon.ico i skopiuj do katalogu /var/www/flaga/static. Ja ze swojego komputera skopiowałam o tak:
```
scp <ścieżka do pliku na komputerze> <skrót do logowania na serwer>:/var/www/flaga/static
```
3. Teraz trzeba umieścić link do tej ikonki w plikach html we flaga/templates. I tu mamy dwie opcje, albo tymczasowo wrzucić do każdego pliku html wewnątrz <head></head>, albo jeśli ktoś już umie w extendowanie to w bazowym pliku html. Link wygląda tak:
```
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
```
4. Po przeładowaniu serwera powinno działać


#### Dodaj kursor z flagą Ukrainy. (Opis autorstwa @Urbid ):
```
https://github.com/KubaBaniak/flag_cursor
```


5. Wrzuć na stronę informację o postaci z wikipedii:


```
pip3 install wikipedia
```
Stwórz we fladze folder `moje_programy` a w nim plik `postac.py` wewnątrz katalogu /var/www/flaga.
Czyli plik /var/www/flaga/moje_programy/postac.py
