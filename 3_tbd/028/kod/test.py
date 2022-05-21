import os
import random
if __name__=='__main__':
    flagi=[]
    for _ in range(2):
        flaga = random.choice(os.listdir('static/flag_image'))
        flagi.append(os.path.join('static/flag_image', flaga))