from secure_data_hasher import encrypt_file
import sys
import os

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        file_to_encrypt = sys.argv[1]
    else:
        print('Usage:\n')
        print('python3 python-kdomanski_zadanie_domowe.py /path/to/file_to_encrypt')
        sys.exit(0)

    if os.path.isfile(file_to_encrypt):
        encrypt_file(file_to_encrypt)
    else:
        print("File:",file_to_encrypt, "not exist")