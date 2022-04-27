## Zadanie domowe

Stwórz działającą podstronę z formularzem "form_b" (rozwiń kod w route form_b). Spytaj się w formularzu np. o link do dobrej muzyki.

Po wykonaniu zadnia - postaraj się dodać je do repozytorium ZPXD w folderze zadań domowych. Jutro (26.04.2022 bedzie tu instrukcja jak to zrobic (gdzies po 18)).

Termin: na środę (27.04.2022) - (ale to zadanie nie musi wyść w 100% - jak coś nie wyjdzie to jest wszystko ok - będziemy rozwijać ten temat w środę 27.04.2022).

**Treść zadania domowego**:

1. Skopiuj folder 'kod' do folderu "zadanie_domowe/zadania" i nazwij go swoim nickiem na discordzie lub githubie np zadanie_domowe/zadania/rozwiazanie_lukaszp/.."
2. Dodaj do niego kod zadania domowego - czyli treść 2 formularza w pliku app.py i w pliku templates/form_b.html
3. Dodaj kod repozytorium:
  a. fork repozytorium
  
  b. dołóż swój folder z rozwiązaniem (utworzony w kroku 1)
  
  c. zrób PR (pull requesta) :)

Jak coś nie wyjdzie to na spokojnie, pierwsze koty za płoty :)

**Uwaga - ważne!**

Po wykonaniu ćwiczenia i sprawdzeniu kodu czy i jak działa - wyhaszuj kod - przyda się na potem. Wróć do niego jak będziesz chciał/chciała znów poćwiczyć, a następnie znów go zahaszuj. 

Po zmianie treści strony - wykonaj:
```
sudo systemctl restart nginx
sudo systemctl restart flaga.service
```
Czyli to co wykonuje skrytp /var/www/flaga/pomocnicze_skrypty/reload.py .
