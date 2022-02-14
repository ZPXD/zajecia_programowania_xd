def print_classes():
    pass


def password(n):
    import random as rnd
    # you can also
    import string as st
# debug #  print(n)
    # określenie klas stringów, z których będą losowane znaki
    cats = [st.ascii_lowercase, st.ascii_uppercase, st.punctuation, st.digits]
    # modyfikacja ilości powtórzeń znaków z kazej klasy w zależności od liczby
    # znaków w haśle
    if int(n) < 8:
# debug #        print("Minimalna liczba znaków hasła to 8!",
# debug #              "Zostanie zwrócone hasło o 8 znakach.", sep="\n")
        min = 2
        max = 8
    else:
        min = int(n/len(cats))
        max = int(len(cats) * min)
# debug #        print("max:", max, "min:", min)
    choice = rnd.choice
    # zamiast:
    # for value in cats:
    #    jakas_funkcja(value)
    # robimy:
    # jakas_funkcja(*cats)
    #
# debug #    print(cats * min + [choice(cats) for _ in range(n - max)])
    # mapuj funkcję choice na listę
    pwd = *map(choice, cats * min + [choice(cats) for _ in range(n - max)]),
    # lista, która będzie iterowana, a na każdym jej elemencie robione
    # mapowanie fukcji
    for i in range(max):
        # losuj indeks mieszania - j
        j = choice(range(i, max))
        pwd = list(pwd)
# debug #        print("pwd to:", pwd, "j is:", j, "i to:", i)
        # zamień miejscami element liczby 'kolejnej' (i)  z elementem
        # o wylosowanym indeksie (j)
        pwd[i], pwd[j] = pwd[j], pwd[i]
# debug #    print(''.join(pwd))
# debug #    print('pwd to', pwd)
    return pwd


n = 16
password = (password(n))
r = ''
# for i in aha:
#    r = r+i
# print(r)
# print(''.join(map(str, password)))
print(*password, sep='')
# debug #print(r, "has length:", len(r))
