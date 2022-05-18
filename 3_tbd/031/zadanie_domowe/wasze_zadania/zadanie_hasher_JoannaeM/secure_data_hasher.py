from cryptography.fernet import Fernet
import os
import sys


'''
Protect files & data.

Simple collection of hashing functions to secure files and data.
1. Access your Fernet key, create it if it does not exist.
2. Encrypts file
3. Decrypts file
4. Get encrypted file contents.
5. Encrypt text and save it as a file.
6. Encrypt text and return it.
7. Decrypt text and return it.

This is very basic set of tools. Dont depend on soily it to protect anything super secret, but it's a good, solid start. There is more.

ZPXD, Łukasz Pintal.
'''
file_path = 'do_testu.txt'


def unlock_key(key_name='.unlock.key'):
    '''
    Figures out whether key exists or not. If not, creates. 

    Returns a key.
    '''

    # Figure out where, who are you at server and what is your key name.
    user = os.environ.get("USER")
    home_folder = '/home/{}'.format(user)
    if user == 'root':
        home_folder = '/{}'.format(user)

    # Default name is '.unlock.key', but you can create new for every file if you want.
    place_for_unlock_key = '{}/{}'.format(home_folder, key_name)

    # Create a key if it does not exists.
    if not key_name in os.listdir(home_folder):
        key = Fernet.generate_key()
        with open(place_for_unlock_key, 'wb') as unlock:
            unlock.write(key)

    # Read a key and return it.
    with open(place_for_unlock_key, 'rb') as unlock:
        key = unlock.read()
    return key


def encrypt_file(file_path, key_name='.unlock.key'):
    '''
    Encrypts file.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print('File {}  encrypted.'.format(file_path))


def decrypt_file(file_path, key_name='.unlock.key'):
    '''
    Decrypts file.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print('File {} decrypted.'.format(file_path))


def get_file_data_and_decrypt(file_path, key_name='.unlock.key'):
    '''
    Opens and decrypts given file. Return decrypted file contents.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
    print('File  {} data read, decrypted, passing it as a variable.'.format(file_path))
    return decrypted_data


def save_encrypted_text(file_path, text, key_name='.unlock.key'):
    '''
    Encrypts text and saves it as a file.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    encrypted_data = f.encrypt(text)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print('Text encrypted and saved to {}'.format(file_path))


def encrypt_text(text, key_name='.unlock.key'):
    '''
    Encrypts text and returns it.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    encrypted_data = f.encrypt(text)
    return encrypted_data


def decrypt_text(encrypted_text, key_name='.unlock.key'):
    '''
    Decrypts text and returns it.
    '''
    key = unlock_key(key_name)
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_text)
    return decrypted_data


if __name__ == "__main__":

    # Default key.
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        encrypt_file(file_path)

    # Named key.
    if len(sys.argv) == 3:
        key_name = sys.argv[2]
        encrypt_file(file_path, key_name)
