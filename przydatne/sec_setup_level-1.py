#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

import os

print("##################")
print("#")
print("# Witaj w skrypcie konfiguracji powiadomień na email")
print("#")
print("# Proszę o odpowiedzenie na kilka pytań.")
print("#")
print("# UWAGA: będzie działać wyłacznie na Ubuntu")
print("#")
print("##################")
while True:
    print()
    key = input('Czy masz konto GMAIL ? (T/N)')
    if key in ["T", "t", "Y", "y"]:
        print()
        host_name = input("Podaj pełną nazwę hosta i domeny (host.adomena.pl): ")
        print()
        email = input(' Podaj twój email: ')
        if email.endswith("@gmail.com"):
            print()
            password = input(' Podaj ustawione hasło aplikacji: ')
            if len(password) < 16:
                print()
                print("Prawdopodobnie wpisane hasło ma za mało znaków.")
                print("Powinno być 16 znaków bez znaków spacji. ")
                print("Zacznijmy od nowa.")
                print()
                continue
            else:
                break
        else:
            print()
            print("Prawdopodobnie podałeś niepoprawny adres email.")
            print("Zacznijmy od nowa.")
            print()
            continue
    elif key in ["N", "n"]:
        print()
        print("Niestety musisz mieć konto GMAIL by skorzystać z tego WIZARD ustawień")
        print("Wróć jak będziesz mieć konto GMAIL")
        print()
        raise SystemExit
    else:
        print()
        print("Niepoprawna odpowiedź")
        print()
        continue
print()
print("Kontynuujemy ...")
print()
print("Instaluje niezbędne pakiety, możesz zostać poproszony o hasło ...")
os.system('sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install postfix mailutils libsasl2-2 ca-certificates libsasl2-modules')
print()
print("Konfiguruje wysyłanie email ...")
sasl_password = 'echo \"[smtp.gmail.com]:587            ' + email + ':' + password +'\" | sudo tee /etc/postfix/sasl_passwd'
os.system(sasl_password)
conf = "\
smtpd_banner = \$myhostname ESMTP \$mail_name (Ubuntu)\n\
biff = no\n\
append_dot_mydomain = no\n\
readme_directory = no\n\
compatibility_level = 2\n\
smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\n\
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\n\
smtpd_tls_security_level=may\n\
smtp_tls_CApath=/etc/ssl/certs\n\
smtp_tls_security_level=may\n\
smtp_tls_session_cache_database = btree:\${data_directory}/smtp_scache\n\
smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination\n\
alias_maps = hash:/etc/aliases\n\
alias_database = hash:/etc/aliases\n\
myorigin = /etc/mailname\n\
relayhost = [smtp.gmail.com]:587\n\
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128\n\
mailbox_size_limit = 0\n\
recipient_delimiter = +\n\
inet_interfaces = loopback-only\n\
inet_protocols = all\n\
smtp_sasl_auth_enable = yes\n\
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd\n\
smtp_sasl_security_options = \n\
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt\n\
smtp_use_tls = yes\n\
"
conf = conf + "myhostname = " + os.uname().nodename + "\n"
conf = conf + "mydestination = "
conf = conf + host_name
conf = conf + ', \$myhostname, ' + os.uname().nodename + ', localhost.localdomain, localhost\n'
os.system('echo \"' + conf + '\" | sudo tee /etc/postfix/main.cf')
os.system('sudo chmod 600 /etc/postfix/sasl_passwd')
os.system('sudo postmap /etc/postfix/sasl_passwd')
print()
print("Kończymy konfiguracje ...")
os.system('sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install logcheck')
os.system('echo \"root: '+email+'\n'+'\"|sudo tee -a /etc/aliases')
os.system('sudo newaliases')
os.system('echo \'EXTRA_OPTS=\"-l\"\'|sudo tee -a /etc/default/cron')
os.system('sudo systemctl restart postfix cron')
print("Sprawdź czy dostaniesz testowy email ...")
test_email = 'echo \"This is the body of an encrypted email\" | mail -s \"Testowy EMAIL\" ' + email
os.system(test_email)
print("Koniec konfiguracji email.")
print()
print("Konfigurujemy powiadamienia o aktualizacji systemu")
print()
os.system('sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install apticron-systemd')
conf_apticron = 'EMAIL=\"' + email + '\"\n'
os.system('echo \"' + conf_apticron + '\"| sudo tee /etc/apticron/apticron.conf')
os.system('sudo systemctl restart apticron')
print()
print("Koniec konfiguracji powiadomień o aktualizacji")
print()
