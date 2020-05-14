import pandas as pd
import matplotlib.pyplot as plt
import os

pd.__version__

def wczytaj_plik(file_path):
    df = pd.read_csv(file_path)
    df.columns = ['datetime', 'Temperatura', 'Wiatr']
    df.set_index('datetime', inplace=True)
    return df

wczytaj_plik(file_path)
path  = 'Test_excel'

file_list =[]
for folder in os.listdir(path):
    for file_ in os.listdir(path + "/" + folder):
        file_list.append(os.path.join(path, folder, file_))

df_all = pd.DataFrame()
for file_ in file_list:
    df = wczytaj_plik(file_)
    df_all = df_all.append(df)


df_all