import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotagem


# Abre um diálogo para selecionar um arquivo Excel e armazena o caminho do arquivo na variável 'arquivo'
arquivo = "MRV/TABELA.xlsx"

# Lê o arquivo Excel selecionado em um DataFrame do pandas
df = pd.read_excel(arquivo)


# Cria uma figura e uma grade de subplots
fig, axes = plt.subplots(3, 4, figsize=(15,10))

# Achata o array de eixos para facilitar a iteração
axes = axes.flatten()


# Itera sobre cada coluna no DataFrame
for i, column in enumerate(df.columns):
    # Plota a contagem de valores da coluna atual como um gráfico de barras no eixo correspondente do subplot
    df[column].value_counts().plot(kind='barh', ax=axes[i], fontsize=6)  
    # Define o título para o subplot atual
    axes[i].set_title(f'Frequencia em {column}', fontsize=8) 
    # Define o rótulo do eixo y para o subplot atual
    axes[i].set_xlabel('Frequencia', fontsize=6)  
    # Rotaciona os rótulos do eixo x para melhor legibilidade e define o tamanho da fonte
    axes[i].tick_params(axis='x', labelsize=6) 

# Ajusta o layout dos subplots para evitar sobreposição
plt.tight_layout()
# Exibe o gráfico
plt.show()
# Salva a figura em um arquivo PDF
fig.savefig("relatorio.pdf")
