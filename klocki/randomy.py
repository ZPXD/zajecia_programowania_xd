import random
from random import sample
losowa_liczba = random.randint(1, 5)
losowy_float_0_1 = random.random ()
losowa_wartosc = random.choice(['a','b','c'])
lista = ['1- and', '2-grs', '3-mt', '4-pw', '5-inny']
lista_2 = [ 'red', 'blue', ';p']
#random.sample(lista_2,k=1)
lista_2_sample = random.choices(lista_2, weights=[20, 25, 1], k=5)
random.shuffle(lista)
# print ('losowa liczba int:',losowa_liczba)
# print ('losowy float:', losowy_float_0_1)
# #print ('losowa z listy to:', losowa_wartosc)
# #print('przetasowana lista to:',lista)
# #print ('wylosowana wartosc to:', sample(lista_2,1))
print ('Moja wagowa lista to:', lista_2_sample)

for i in range(5):
    random.seed(3)
    print(random.randint(1,1000))
    print(random.randint(1,1000))

