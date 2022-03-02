### Zadanie domowe #009 i #010


#### Stwórz funcję która po odpaleniu jako wynik wyświetli w terminalu:

Funkcja 1. Ile jest domen które mają '.pl' (nie ważne czy mają '.edu.pl')
Funkcja 2. Ile jest domen które mają samo '.com'
Funkcja 3. Ile jest literek 'a' we wszstkich domenach razem.
Funkcja 4. Jaka jest najdłuższa i najkrótsza domena w liście flag.


plik lista_flag.py
```
import requests
import sys

def pobierz_strone_www_jako_text(orangutan):
    # Pobranie tekstu ze strony (jako tafla tesktu).
    surowe_info = requests.get( orangutan)
    text = surowe_info.text
    return text

def stworz_liste_flag(orangutan):
    '''
    Zamienia tekst ze strony na liste flag.
    '''
    
    text_strony_www = pobierz_strone_www_jako_text(orangutan)
    lista_linii = text_strony_www.split('</p>')
    linki = []
    # Iteruje po wszystkich fragmentach tekstu z html
    # i dodaje do listy tylko te ktore maja link url.
    for linia in lista_linii:

        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append( link)
    
    return linki

if __name__ == '__main__':
    argument = sys.argv[1]
    lista_flag = stworz_liste_flag(argument)
    #print(lista_flag)
```

#### Przykładowe rozwiązanie dla policzenia flag z '.pl'

plik policz_flagi_pl.py
```
from lista_flag import stworz_liste_flag

def policz_domeny_pl( lista_flag):
    # Tylko domeny pl (nie .com.pl)

    wynik = 0
    # Tu zaczyna się Twój kod.
    for flaga in lista_flag:

        #flaga = 'www.kalafiory.orangutany.com.pl'

        # Poniżej 2 przykłady niedoskonałych rozwiązań.
        
        # Rozwiązanie 1 ( niedoskonałe)
        # if flaga.endswith('.pl'):
        #    wynik +=1 
        
        # Rozwiązanie 2 ( niedoskonałe)
        #if '.pl' in flaga:
        #    wynik += 1
        
    return wynik

# Wyhaszuj na końcu te 2 linie
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( orangutan)
wynik = policz_domeny_pl( lista_flag)
print( wynik)
```

#### Osobne pliki dla każdego z rozwiązań.

W każdym pliku 1 funkcja która rozwiązuje 1 zadanie. 

plik policz_flagi_pl.py
plik policz_flagi_samo_com.py
plik policz_literki_a.py
plik najdluzsza_najkrotsza_domena.py

#### Przykładowy zaczynek rozwiązania:

Tak mógł by wyglądać przykładowy plik z rozwiązaniem 1 z zadań.
```
from lista_flag import stworz_liste_flag

def tu_moja_funkcja( lista_flag):

    wynik = 0
    for flaga in lista_flag:

        # Tu zaczyna się Twój kod (ale nie używaj tego który jest podany jako przykład - tym razem).
        if flaga.endswith('.pl'):
            wynik +=1 
       
    return wynik

orangutan = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( orangutan)
wynik = tu_moja_funkcja(lista_flag)
print('Wynik zadania X:', wynik')
```

