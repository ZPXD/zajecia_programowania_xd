from lista_flag import stworz_liste_flag
import re


def policz_domeny_pl(lista_flag): # lista=[] rozwiązuje problem nie zdefiniowanej zmiennej
    # Tylko domeny .pl (nie .com.pl)

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
        if '.pl' in flaga:
            wynik += 1
        if flaga.count('.pl'):
            #wynik +=
            wynik += 1
        #if flaga.count():

    # Tu kończy się Twój kod.
    return wynik


def oczysc_flage(flaga):
    '''
    Czyści flagę z początkowego 'http[s]://'
    oraz końcowych: ':\d', '/+.*'.
    Zwraca nazwę domeny, np: 'www.ziemniak.pl'
    (zamiast początkowego: 'https://www.ziemniak.pl/o_mnie:8080')
    '''
    pass
    # dopisać w oparciu o regexp
    # podane wyżej. Najpierw uciąć początek na wypadek gdyby było jakieś:
    # www.https://sdfsdf/http://mojastrona.pl # niepoprawne, ale jako string
    # jest to możliwe (np. złe wpisanie przez użytkownika)


def split_flagi():
    '''
    Pobiera link(str), tnie delimiterem '.' i zwraca wyrazy(list)
    '''
    flaga = 'https://www.kalafiory.orangutany.com.pl:8080'
    return flaga.split('.')

print(split_flagi())
# Wyhaszuj na końcu te 2 linie
# wynik = policz_domeny_pl( linki)
# print( wynik)


tld_list = [
'com',
'edu',
'gov',
'biz']


orangutan = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag(orangutan)
wynik = policz_domeny_pl(lista_flag)
print(wynik)
