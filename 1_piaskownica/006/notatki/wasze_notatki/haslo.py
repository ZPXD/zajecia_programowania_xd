import random
import string


# hasło
# - string - ciąg znaków
# -
n_znakow = 8
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
wszystkie_znaki = lowercase + uppercase + punctuation + digits

losowe_znaki = random.sample(wszystkie_znaki, 8)
haslo = ''.join(losowe_znaki)


# '.join(random.choice(string.ascii_letters) for _ in range(10))

# Zadanie domowe:
#
# Udoskonalić generator haseł tak, aby:
# 1. brał po 2 losowe cyfry/znaki i duze/male litery
# 2. losowa kolejność cyfr, znaków, dużych i małych liter
# 3. Pogłówkujcie, co robić, aby to działało dobrze dla zadanej
#    liczby znaków od 8 do 20
#
# Zadanie domowe trzymamy u siebie na serwerze i
# w poniedzałęke będzie omówione jak będziemy
# gromadzić zadania domowe, projekty,
# i też parę słów o GIT i VSC

print()
print(haslo)
print()
