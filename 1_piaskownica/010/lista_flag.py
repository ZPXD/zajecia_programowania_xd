import requests
import sys
# import tld
import re


def pobierz_strone_www_jako_text(orangutan):
    # Pobranie tekstu ze strony (jako tafla tekstu).
    surowe_info = requests.get(orangutan)
    text = surowe_info.text
    return text


def stworz_liste_flag(orangutan):
    '''
    Zamienia tekst ze strony na listę flag.
    '''
    # Przygotowanie listy linków ze strony :)
    text_strony_www = pobierz_strone_www_jako_text(orangutan)
    lista_linii = text_strony_www.split('</p>')
    linki = []
    # Iteruje po wszystkich fragmentach tekstu z html
    # i dodaje do listy tylko te, ktęre mają link url.
    for linia in lista_linii:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append(link)

    return(linki)


def czy_prawidlowa_domena(str):
    '''
    Zwraca true/false dla podanego stringu.
    Domena jest prawidłowa, gdy:
    1. Zawiera litery a-z, A-Z albo cyfry 0-9 lub znak '-'
    2. Jej długość mieści się w zakresie 1-63 znaki.
    3. Nie zaczyna się i nie kończy znakiem '-'
    4. Ostatnia Top Level Domain musi liczyć od 2-6 znaków
    5. Nazwa domeny może mieć subdomenę (np. host.domena.pl)
    '''
    # regex =


def get_tld(domena):
    from tld import get_tld
    get_tld(domena, fix_protocol=True)
    # in: 'www.google.co.uk'
    # out: 'co.uk'


def get_fld(domena):
    from tld import get_fld
    get_fld(domena, fix_protocol=True)
    # in: 'www.google.co.uk'
    # out: 'google.co.uk'


if __name__ == '__main__':
    argument = sys.argv[1]
    lista_flag = stworz_liste_flag(argument)
