import random
import string
import sys

def generate_password(num_characters):
    # Create shuffled list of 4 char sets, each of unique chars.
    char_sets_base = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]
    char_sets_now = char_sets_base.copy()
    random.shuffle(char_sets_now)

    # Iterate over each char_set list element, and regenerate it to the full. 
    password = []
    for i in range(num_characters):

        # If char_sets_now are empty, it reloads it to char_sets_base state.
        if len(char_sets_now) == 0:
            char_sets_now = char_sets_base.copy()
            # Shuffle it again to ensure randomnes.
            random.shuffle(char_sets_now)
        
        # Pick a char_set.
        char_set = char_sets_now.pop()
        # Pich 1 char.
        char = random.choice(char_set)
        # Add it to the password.
        password.append(char)
        
    # Shuffle password characters.
    random.shuffle(password)
    password = ''.join(password)
    return password

if __name__ == "__main__":
    num_characters = int(sys.argv[1])
    password = generate_password(num_characters)
    print(password)
