import funkcje

def password(n):
    import secrets
    import string as S
    of = secrets.choice
    cats = [S.ascii_lowercase, S.ascii_uppercase, S.punctuation, S.digits]
    pwd = *map(of, cats * 2 + [of(cats) for _ in range(n - 8)]),
    for i in range(8):
        j = of(range(i, n))
        pwd = list(pwd)
        pwd[i], pwd[j] = pwd[j], pwd[i]
    return pwd


aha = (password(9))
r = ''
for i in aha:
    r = r+i
    r = rozliterkowanie('a')
print(r)
