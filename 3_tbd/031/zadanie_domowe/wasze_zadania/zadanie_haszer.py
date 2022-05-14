import sys
from tower_cybersecurity.scripts.secure_data_hasher import encrypt_file

if __name__ == "__main__":
    	
	# Default key.
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		encrypt_file(file_path)