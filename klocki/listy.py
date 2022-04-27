lista = [ 'b', 'c', 'b', 'z', 'b', 'a']

'''szukany_element = 'a'
n_b = lista.count('b')
print ("ilość be: ",n_b)
i = lista.index( szukany_element)
print('Szukany element jest na indexie:',i)'''

lista_i = []
for i in range (len(lista)):
    temp_i = lista.index('a', i)
    if temp_i not in lista_i:
        lista_i.append(temp_i)
print(lista_i)