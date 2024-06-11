from tkinter.filedialog import askopenfilename  # Importa a função para abrir um diálogo de seleção de arquivo
import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotagem
import math  # Importa o math para operações matemáticas

# Abre um diálogo para selecionar um arquivo Excel e armazena o caminho do arquivo na variável 'arquivo'
arquivo = askopenfilename()

df = pd.read_excel(arquivo)

relatorio = open("relatorio.txt","w")


for column in df.columns:
    relatorio.write("{}\n".format(column))
    relatorio.write(df[column].value_counts().to_string())
    relatorio.write("\n----------------------------\n\n")

relatorio.close()


