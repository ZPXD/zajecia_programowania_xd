import requests

# Pobranie tekstu ze strony (jako tafla tesktu).
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( orangutan)
text = surowe_info.text

# Przygotowanie listy linków ze strony :)
lista_linii = text.split('</p>')
linki = []
for linia in lista_linii:

    link = linia.replace('<p>', '')
    link = link.replace('- ', '')
    link = link.strip()
    if ' ' in link or '<' in link:
        continue
    linki.append( link)

# CEL:
# Policz ile jest domen z .pl

# Realizacja :)
domeny_pl = 0
domeny_com = 0
domeny_x = 0

# Ile jest wszystkich kropek w sumie we wszystkich linkach:
wszystkie_kropki = 0

for i, link in enumerate(linki):

    if '.pl' in link:
        domeny_pl += 1
    if '.com' in link:
        domeny_com += 1
    if ('.pl' in link) and ('.com' in link):
        domeny_x += 1

    # Policz ile jest kropek w podanym stringu ("link")/
    n_kropek = link.count('.')
    wszystkie_kropki + n_kropek

print(wszystkie_kropki)
