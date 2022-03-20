### CRON - CROND - CRONTAB

Opracowanie WojRep (WRepińskiego).

cron - generalnie nazwa usługi, która w zaplanowany sposób wywołuje akcje (uruchamia skrypty).
crond - daemon (usługa), która uruchamia w tle zaplanować akcje zdefiniowane w plikach konfiguracyjnych crontab
crontab - ogólnie pliki zawierające informacje dot uruchamiania akcji.

crond pozwala uruchamiać akcje w zaplanowanych cyklach, które definiujemy poprzez podanie minuty, godziny, dnia, miesiąca, dnia tygodnia, czyli tym się definiuje cykliczność tej akcji.

#### Pliki cron'a:

UWAGA: Bez dogłębnej wiedzy nie należy modyfikować ręcznie plików:
/etc/crontab
/etc/cron.d/*
/etc/cron.daily/*
/etc/cron.hourly/*
/etc/cron.weekly/*
/etc/cron.montly/*

#### Zapis w cron

Zdecydowanie zaleca się konfiguracje cron wyłącznie poprzez polecenie crontab -e (dla danego zalogowanego użytkownika) lub poprzez crontab -e -u USER dla użytkownika o loginie USER.
Struktura pliku crontab:
m h dom mon dow     commend
gdzie:
m - minuta
h - godzina
dom - numer dnia miesiąca
mon - numer miesiąca
dow - dzień tygodnia, wartość 0/7 odpowiada za niedzielę, 1 to poniedziałek, 2 to wtorek i tak dalej ...

#### Wartości:

Dozwolone znaki: *, ,, -, /

* - określa, że zadanie bedzie się zawsze wykonywać dla miejsca zdefiniowania, inaczej "ANY"
, - po przecinku określamy kolejne wartości dla których wywołujemy akcję
- - określamy przedział
/ -  określamy co ile ma sie powtórzyć akcja

w polach m, h, dom, mon, dow podajemy wartości liczbowe lub wartości w przedziałach, przykłady:
0 5 * * 1   python3 script.py => uruchomienie komendy python3 script.py co tydzień w poniedziałek o 05:00 rano.
* * * * *   python3 scritp.py => uruchomienie komendy python3 script.py co 1 minutę
*/5 * * * *   python3 script.py => uruchamianie komendy python2 script.py co 5 minut
2,5,8 4,7,20 * * *   python3 script.py => uruchamianie komendy python2 script.py w 2, 5 i 8 minucie dla godzin 4,7 i 20
15 2-6 * * *   python3 script.py => uruchamianie komendy python2 script.py o czasie: 2:15, 3:15, 4:15, 6:15

#### Pomoc do generowania linii crontab:
- https://crontab-generator.org/
- https://crontab.guru/

#### Wiedza po Polsku:
- https://ai.ia.agh.edu.pl/_media/pl:dydaktyka:unix:gjn-cron.pdf
- https://www.arubacloud.pl/poradnik/jak-zarzadzac-planowanymi-operacjami-z-crontab-na-centos-8.aspx
- https://webinsider.pl/raspberry-pi-linux-cron/