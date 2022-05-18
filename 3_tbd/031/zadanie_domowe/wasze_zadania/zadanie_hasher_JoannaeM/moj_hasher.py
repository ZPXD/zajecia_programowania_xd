from secure_data_hasher import encrypt_file

my_file = 'do_testu.txt'
encrypt_file(my_file)
text = open(my_file).read()
print(text)
