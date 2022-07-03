from tower_cybersecurity.scripts.secure_data_hasher import encrypt_file

# 1st version:
# import sys
# if sys.argv[1]:
#     file_path = sys.argv[1]
#     encrypt_file(file_path)

# 2nd version:
print('Provide the file to encrypt:')
file_path = input()
encrypt_file(file_path)

