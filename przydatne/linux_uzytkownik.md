## Użytkownik na Linux Ubuntu 18/20


### Root.

Powinieneś być już root. Robiliśmy to w [Etap 4 w kroku 6](https://github.com/ZPXD/flaga/blob/main/instrukcje/etap_4_3_zdobadz_serwer_polaczenie.md). Sprawdź to:
```
echo $USER
```
Jak pokazuje root to idź do kroku 2. Jeżeli nie, utwórz hasło dla root wpisując:
```
sudo passwd
sudo su
```
I sprawdź znów pisząc "echo $USER", aż będzie pokazywać root. Jak masz błąd, wróć do etapu 4.3 lub spytaj na grupie o pomoc.

Jeżeli wszystko zrobiłeś prawidłowo, pojawi Ci się: **root**. Chyba, że jesteś na AWS, to pokaże Ci się **ubuntu**. Root to coś jak administrator. Ma nawet swój folder o ścieżce /root do którego tylko on ma dostęp. Wszystko co ma przypisane uprawnienia **root** możesz robić z jego poziomu. Ty jednak chcesz stworzyć nowego użytkownika. 

Jednak najpierw, minuta dla AWS'owców.

### Użytkownik

Użytkownik to to jako kto jesteś na serwerze. Zwykli użytkownicy mają inne uprawnienia niż root. Nie mogą robić pewnych rzeczy i wchodzić w pewne miejsca.

Napisz w terminalu poniższy kod zamieńiając XXX na nazwę jaką chcesz mieć jako użytkownik Twojego serwera.
Nazwa nie może zawierać spacji i specjalnych znaków.
```
NEW_USER=XXXX
```
Stworzyłeś zmienną NEW_USER. Teraz możesz ją wywoływać zawsze pisząc jej nazwę ze znakiem dolara.
```
echo $NEW_USER
```

#### Tworzymy użytkownika.

Czas stworzyć użytkownika o takiej nazwie jak chcesz.

Będziesz pytany o numer telefonu, pokoju i inne rzeczy - wszystko pomijaj naciskając enter.

Wklej poniższy kod aby stworzyć użytkownika o takiej nazwie jaką wartość przypisałeś do NEW_USER.
```
adduser $NEW_USER --gecos GECOS --disabled-password --force-badname
```
I poniższy kod aby przypisać go do grupy www-data (potrzebnej np. do postawienia strony www) i do grupy sudo (potrzebnej do wykonywania operacji z poziomu użytkownika **root**).


```
adduser $NEW_USER www-data
adduser $NEW_USER sudo
```

Sprawdź czy jesteś w grupie sudo i www-data:
```        
groups $NEW_USER 
```
Wyświetli się: $NEW_USER : $NEW_USER www-data sudo. Jak nie ma sudo i www-data, to pominąłeś krok wyżej.

#### Usuń użytkownika:

```
deluser <nazwa_uzytkownika>
```

#### Pozwólmy działać naszemu użytkownikowi bez hasła na serwerze (i tak będziesz łączyć się przez klucz).

Komendą echo "wrzucamy" jedną linię która to robi do pliku konfiguracyjnego sudoers.
```
echo "$NEW_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

#### Katalog domowy.

Od teraz też masz swój nowy domowy katalog. Narazie nic tam nie ma. Gdy będziesz się logował na swojego użytkownika, tutaj będziesz się pojawiał
```
cd /home/$NEW_USER
pwd
```
