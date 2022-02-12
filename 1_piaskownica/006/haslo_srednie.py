import random
import string

# Generator Hasła 
# - string - ciag znakow 
# - losowe hasło
# - okreslona ilosc znakow - ponad 8
# - Duże litery, 2
# - Małe litery, 2
# - Znaki specjalne, 2
# - Cyfry, 2

n_znakow = 8 
n_znakow_typu = 2

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
wszystkie_znaki = lowercase + uppercase + punctuation + digits

losowe_znaki = random.sample(wszystkie_znaki, n_znakow)
haslo = ''.join(losowe_znaki)

print()
print(haslo)
print()

# Zadanie domowe:

# Udoskonalić generator haseł tak aby:
# 1. brał po 2 losowe cyfry/znaki i duze/male litery
# 2. losowa kolejnosc cyfr, znakow, duzych i malych liter
# 3. Pogłówkujcie co robic aby to dzialalo dobrze dla zadanej
#    liczby znakow od 12 do 20 
