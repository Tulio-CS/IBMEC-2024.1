from tkinter.filedialog import askopenfilename  # Importa a função para abrir um diálogo de seleção de arquivo
import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotagem
import math  # Importa o math para operações matemáticas

# Abre um diálogo para selecionar um arquivo Excel e armazena o caminho do arquivo na variável 'arquivo'
arquivo = askopenfilename()

# Lê o arquivo Excel selecionado em um DataFrame do pandas
df = pd.read_excel(arquivo)

# Obtém o número de colunas no DataFrame
num_columns = len(df.columns)

# Define o número de colunas na grade de subplots
ncols = 5
# Calcula o número de linhas necessárias para a grade de subplots
nrows = math.ceil(num_columns / ncols)

# Cria uma figura e uma grade de subplots
fig, axes = plt.subplots(nrows, ncols, figsize=(15,10))

# Achata o array de eixos para facilitar a iteração
axes = axes.flatten()


# Itera sobre cada coluna no DataFrame
for i, column in enumerate(df.columns):
    # Plota a contagem de valores da coluna atual como um gráfico de barras no eixo correspondente do subplot
    df[column].value_counts().plot(kind='bar', ax=axes[i], fontsize=8)  
    # Define o título para o subplot atual
    axes[i].set_title(f'Frequencia em {column}', fontsize=10) 
    # Define o rótulo do eixo x para o subplot atual
    axes[i].set_xlabel(column, fontsize=8)  
    # Define o rótulo do eixo y para o subplot atual
    axes[i].set_ylabel('Frequencia', fontsize=8)  
    # Rotaciona os rótulos do eixo x para melhor legibilidade e define o tamanho da fonte
    axes[i].tick_params(axis='x', rotation=90, labelsize=8) 

# Ajusta o layout dos subplots para evitar sobreposição
plt.tight_layout()
# Exibe o gráfico
plt.show()
# Salva a figura em um arquivo PDF
fig.savefig("relatorio.pdf")
