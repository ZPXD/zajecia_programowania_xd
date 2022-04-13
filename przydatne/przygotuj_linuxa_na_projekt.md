## 1. Przygotowanie wymaganego oprogramowania do uruchomienia standardowych projektów na serwerze:

Potrzebujesz na serwerze Linuxie Ubuntu co następuje: 
1. python3
2. pip3 
3. venv
4. git
 
Jeżeli czegoś Ci brakuje, uruchom skrypt `server_preparation_for_project.sh` zdalnie wpisując:
```
wget -q 'https://raw.githubusercontent.com/ZPXD/zajecia_programowania_xd/main/przydatne/server_preparation_for_project.sh' && chmod +x server_preparation_for_project.sh && ./server_preparation_for_project.sh;
```

Skrypt uruchomi poniższe polecenia:
```
apt update
apt install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools --yes
apt install python3-pip
apt install git
pip3 install virtualenv 
```
