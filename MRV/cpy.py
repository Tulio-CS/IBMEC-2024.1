from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
import math

arquivo = askopenfilename()


df = pd.read_excel(arquivo)




fig = plt.figure()

for column in df.columns:
    if df[column].dtype in ['int64', 'float64', 'object']:  # You can adjust the condition based on your needs
        plt.figure(figsize=(10, 6))
        df[column].value_counts().plot(kind='bar')
        plt.title(f'Frequency of values in {column}')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        

fig.savefig("faa.pdf")