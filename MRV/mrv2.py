import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotagem


#Caminho onde a tabela esta armazenada
arquivo = "MRV/TABELA.xlsx"

# Lê o arquivo Excel selecionado em um DataFrame do pandas
df = pd.read_excel(arquivo)


# Cria uma figura e uma grade de subplots
quadro, espacos = plt.subplots(3, 4, figsize=(15,10))
#Funçoes
# subplots(numero de linhas, numero de colunas, tamanho do grafico)

#Argumentos
# numero de linhas em nosso caso 3
# numero de colunas em nosso caso 4

# Achata os de espaços para facilitar na hora de desenhar o grafico
espacos = espacos.flatten()



for numero_coluna, coluna in enumerate(df.columns):
    # Desenha o grafico da coluna desejada no espaco desejado
    df[coluna].value_counts().plot(kind='barh', ax=espacos[numero_coluna], fontsize=6) 
    # df[coluna] = valores na coluna desejada

    #Funçoes
    # value_counts(kind,ax,fontsize) = Função que retorna a frequencia dos valores na coluna
    # plot() = função que desenha o grafico 

    #Argumentos
    # kind = tipo de grafico no nosso caso barh (barra horizontal)
    # ax =  espaço onde o grafico sera desenhado
    # Fontsize = tamanho da fonte

    # -----------------------------------------------------------
    
    # Escreve um titulo no grafico atual
    espacos[numero_coluna].set_title(f'Frequencia em {coluna}', fontsize=6) 

    #Funçoes
    # Set_title(titulo,fontsize) = função que escreve o titulo

    # Argumentos 
    # Titulo = texto que sera escrito, em nosso caso frequemcia em + nome da coluna
    # Fontsize = tamanho da fonte

    # -----------------------------------------------------------

# Ajusta o layout dos graficos para evitar que um grafico fique em cima do outro
plt.tight_layout()
# Exibe o gráfico
plt.show()
# Salva a figura em um arquivo PDF
quadro.savefig("relatorio.pdf")
