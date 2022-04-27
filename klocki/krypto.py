import random

a = sorted(random.sample(range(10,100), 8))
print (a)

def search (l,x):
    for i,y in enumerate(l):
        if y == x :
            return i
        print()
    else:
        raise Exception()
