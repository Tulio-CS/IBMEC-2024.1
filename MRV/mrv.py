from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
import math

arquivo = askopenfilename()


df = pd.read_excel(arquivo)

num_columns = len(df.columns)


ncols = 5
nrows = math.ceil(num_columns / ncols)
print(nrows)

fig, axes = plt.subplots(nrows, ncols, figsize=(15,10))

axes = axes.flatten()


for i, column in enumerate(df.columns):
    df[column].value_counts().plot(kind='bar', ax=axes[i], fontsize=8)  
    axes[i].set_title(f'Frequencia em {column}', fontsize=10) 
    axes[i].set_xlabel('Nome', fontsize=8)  
    axes[i].set_ylabel('Frequencia', fontsize=8)  
    axes[i].tick_params(axis='x', rotation=90, labelsize=8) 



plt.tight_layout()
plt.show()
fig.savefig("foo.pdf")