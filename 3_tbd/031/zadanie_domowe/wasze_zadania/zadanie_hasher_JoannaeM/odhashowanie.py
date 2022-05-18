from secure_data_hasher import decrypt_file

my_file = 'do_testu.txt'
decrypt_file(my_file)
text = open(my_file).read()
print(text)
