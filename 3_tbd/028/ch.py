from os import rename, listdir

if __name__=="__main__":
    files = [x for x in listdir('.') if not x.endswith('.py')]
    for file in files:
        rename(file, f"{file}.jpg")