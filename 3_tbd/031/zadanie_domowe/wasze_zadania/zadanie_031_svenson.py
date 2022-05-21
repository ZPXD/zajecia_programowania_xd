from secure_data_hasher import encrypt_file, decrypt_file

path_file = ""
#decrypt_file("/home/michal/zadania_domowe/031/text.txt")
def encrypt_my_txt_file():
    global path_file
    path_file = input("# Type file's path to be encrypted:\n")
    encrypt_file(path_file)
    print("\n\n# Content of encrypted file: \n\n")

    with open(path_file, "r") as f:
	    encrypted_content = f.read()
    print(encrypted_content, '\n\n')


def decrypt_my_txt_file():
    global path_file
    path_file = input('If you want to decrypt the file \n{} \nPress ENTER \n\nIf you want to decrypt another file, \nType its path and press ENTER \n'.format(path_file)) or path_file
    decrypt_file(path_file)
    print("\n\n# Content of decrypted file: \n\n")

    with open(path_file, "r") as file:
	    decrypted_content = file.read()
    print(decrypted_content, '\n\n')

if __name__ == "__main__":
    encrypt_my_txt_file()
    decrypt_my_txt_file()