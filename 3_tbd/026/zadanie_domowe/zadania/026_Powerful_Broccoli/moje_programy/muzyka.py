import pandas as pd

def read_music():
    df = pd.read_csv('dane/form_data.csv')
    df.values.tolist()
    return reversed(df.values.tolist())

#print(read_music())