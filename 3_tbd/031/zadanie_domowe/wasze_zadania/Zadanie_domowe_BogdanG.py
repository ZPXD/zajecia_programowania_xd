from cryptography.fernet import Fernet
import os
import sys


def unlock_key(key_name): # adoptowano do potrzeb

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

def encrypt_file(file_path, key_name): # adoptowano do potrzeb
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
############# praca domowa #######################
klucz=input("podaj klucz:")
plik=input("Podaj ścieżkę do pliku:")
unlock_key(klucz)
encrypt_file(plik, klucz)
##################################################