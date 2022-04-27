import requests

url = 'https://rolniknysa.pl/'

def simple_crawler(url):
    stronka = requests.get(url).text
    linki = stronka.split('href="')
    linki_python = []
    for l in linki:
        link = l.split('"')[0]
        if 'http' in link:        
            if 'nysa' in link:
                linki_python.append(link)
    return linki_python

linki_python = simple_crawler(url) # 295
linki_python = list(set(linki_python))
w_sumie = len(linki_python)
all_links = linki_python.copy()

while linki_python:
    link = linki_python.pop(0)
    nowe_linki = simple_crawler(link)
    nowe_linki_ok = []
    for link in nowe_linki:
        if link not in all_links:
            all_links.append(link)
            nowe_linki_ok.append(link)
    linki_python.extend(nowe_linki_ok)
    print(len(linki_python))