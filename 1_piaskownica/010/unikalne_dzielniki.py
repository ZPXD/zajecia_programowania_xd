import sympy as sp
'''
Napisaliśmy z Filipem taki kod, może chcecie się pobawić. Zadanie na 6 robił
do matury czy coś.

wymaga pliku liczby.txt w stylu:

234234
32
24243

Wymaga instalacji sympy.

pip3 install sympy

Wylicza dla zadanych liczb jej unikalne dzielniki spośród liczb pierwszych i
jeżeli są dokładnie 3 to zapisuje w 2 pliku.
'''
sciezka_pliku_wejsciowego = 'liczby.txt'
sciezka_pliku_wyjsciowego = 'legitne_liczby.txt'


def pobierz_liczby():
    with open(sciezka_pliku_wejsciowego, 'r') as f:
        liczby = f.readlines()
        liczby = [int(l.strip()) for l in liczby]

    print('Zadane liczby:', liczby)
    return liczby


def zapisz_liczby(liczby):
    with open(sciezka_pliku_wyjsciowego, 'w+') as f:
        for l in liczby:
            f.write(str(l)+'\n')


def znajdz_dzielniki(liczba):
    dzielniki = []
    for i in range(1,liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki


def znajdz_dzielniki_pierwsze(l):
    liczby = [l]
    dzielniki_fin = []
    while liczby:
        i = liczby.pop()
        dzielniki = znajdz_dzielniki(i)
        for d in dzielniki:
            if sp.isprime(d):
                if d in dzielniki_fin:
                    pass
                else:
                    dzielniki_fin.append(d)
            else:
                liczby.append(d)
    return dzielniki_fin


def zadanie_5_przez_10(n_dzielnikow):
    liczby = pobierz_liczby()
    legitne_liczby = []
    for l in liczby:
        dzielniki = znajdz_dzielniki_pierwsze(l)
        print('- Liczba i jej dzielniki:', l, dzielniki)
        if len(dzielniki) == n_dzielnikow:
            legitne_liczby.append(l)

    print('Legitne liczby:')
    print(legitne_liczby)
    zapisz_liczby(legitne_liczby)

n_dzielnikow = 3
zadanie_5_przez_10(n_dzielnikow)
