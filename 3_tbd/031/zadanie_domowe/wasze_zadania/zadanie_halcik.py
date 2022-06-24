import sys

from secure_data_hasher import encrypt_file

#print(sys.argv, type(sys.argv))

#print(sys.argv[1])
file_path = sys.argv[1]
encrypt_file(file_path)
