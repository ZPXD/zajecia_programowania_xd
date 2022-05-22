Problem z logowaniem do VSC - permission denied - linux

Jeżeli po zaoraniu serwera i postawieniu go na nowo zgodnie z szybką ścieżką ASAP:

https://github.com/ZPXD/flaga

Masz problem z zalogowaniem się na użytkownika którego stworzyłeś np. 'testowy', zrób check poniższych kroków:

[1] otwórz w VSC plik config - jeśli nie wiesz gdzie znajduje się w VSC, to możesz otworzyć go rownież lokalnie /user/.ssh/ wewnątrz tego folderu znajduje się plik config a wewnątrz tego pliku wpisy dotyczące logowania np:


  Host ubuntu
  HostName HOST_ADRES
  IdentityFile NAZWA_KLUCZA.PEM
  User ubuntu

  Host testowy
  HostName HOST_ADRES
  IdentityFile ~/.ssh/klucz_
  User testowy


[2] Ważna jest weryfikacja czy wpisy są poprawne, jeśli tak to przejdź do terminala lokalnie i w terminalu otwórz ścieżkę user/.ssh/ a następnie wpisz poniższe polecenia, które zmienią poziom uprawnień do folderu i pliku. Żeby VSC mógł posługiwać się kluczem potrzebne jest dostęp:

Folder / plik	Uprawnienia
.ssh w twoim folderze użytkownika	chmod 700 ~/.ssh
.ssh/config w twoim folderze użytkownika	chmod 600 ~/.ssh/config
.ssh/id_rsa.pub w twoim folderze użytkownika	chmod 600 ~/.ssh/klucz_

[3] Następnie zamknij otwarte połączenia w VSC lub cały VSC potem otwórz w folderze .ssh/ plik known_hosts  usuń wpisy, które się tam znajdują po czym włącz ponownie VSC i spróbuj się zalogować na nowego usera 
