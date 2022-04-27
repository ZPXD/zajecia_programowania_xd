## Zadanie domowe

Stwórz działającą podstronę z formularzem "form_b" (rozwiń kod w route form_b). Spytaj się w formularzu np. o link do dobrej muzyki.

Po wykonaniu zadnia - postaraj się dodać je do repozytorium ZPXD w folderze zadań domowych. Jutro (26.04.2022 bedzie tu instrukcja jak to zrobic (gdzies po 18)).

Termin: na środę (27.04.2022) - (ale to zadanie nie musi wyść w 100% - jak coś nie wyjdzie to jest wszystko ok - będziemy rozwijać ten temat w środę 27.04.2022).

### Tu wrzucajcie wasze odpowiedzi na zadania 

1. Pobierz to repozytorium (git clone)
2. Znajdź szablon w pobranym repozytorium - jest w "ZPXD/zajecia_programowania_xd/3_tbd/026/zadanie_domowe/zadania/000_SZABLON_ZADANIA_zmien_nazwe"
3. Skopiuj go i zmień nazwę folderu "/zadanie_domowe/zadania/000_SZABLON_ZADANIA_zmien_nazwe" na nazwę jaką masz na githubie lub discordzie
4. Wedjdź w folder i zrób zadanie. Zapisz.
5. Zrób Pull Requesta (PR)

### Uwaga - ważne!

Po wykonaniu ćwiczenia i sprawdzeniu kodu czy i jak działa - wyhaszuj kod - przyda się na potem. Wróć do niego jak będziesz chciał/chciała znów poćwiczyć, a następnie znów go zahaszuj. 

Po zmianie treści strony - wykonaj:
```
sudo systemctl restart nginx
sudo systemctl restart flaga.service
```
Czyli to co wykonuje skrytp /var/www/flaga/pomocnicze_skrypty/reload.py .
