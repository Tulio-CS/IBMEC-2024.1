import pandas as pd
from math import sqrt
path = "fio de cobre\df.xlsx"
xlsx = pd.ExcelFile(path)


def distancia_euclidiana(p1,p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_sheet(path):
    xlsx = pd.ExcelFile(path)
    for i , sheet in enumerate(xlsx.sheet_names):
        print("{} {}".format(i,sheet))
    pagina = int(input("Selecione uma pagina para ser estudada :\n"))
    return xlsx.sheet_names[pagina]

def get_matrix(path):
    sheet = get_sheet(path)
    df = pd.read_excel(path,sheet_name=sheet)
    df_coords = df[['Latitude WGS84', 'Longitude WGS84']].dropna()
    matriz = [[0] * len(df) for i in range(len(df))]
    for i in range(len(df_coords)):
        for j in range(i+1,len(df_coords)):
            dist = distancia_euclidiana((df_coords.iloc[i]["Latitude WGS84"],df_coords.iloc[i]["Longitude WGS84"]),(df_coords.iloc[j]["Latitude WGS84"],df_coords.iloc[j]["Longitude WGS84"]))
            matriz[i][j] = dist
            matriz[j][i] = dist
    #print(f"lat {df_coords.iloc[32]["Latitude WGS84"]} long {df_coords.iloc[32]["Longitude WGS84"]}")
    #print(f"lat {df_coords.iloc[51]["Latitude WGS84"]} long {df_coords.iloc[51]["Longitude WGS84"]}")
    #print(matriz[32][51])
    return matriz

def caixeiro(matriz,inicio):

    caminho=[0]*len(matriz)
    distancia_percorrida=0
    caminho[inicio] = 1
    rota = [inicio]
    atual = inicio
    for i in range(1,len(matriz)):
        Menor=float("inf")
        cidade_mais_perto=None
        for j in range(len(matriz)):
            if matriz[atual][j] < Menor and caminho[j] == 0:
                cidade_mais_perto = j
                Menor =  matriz[atual][j]

        caminho[cidade_mais_perto] = i
        rota.append(cidade_mais_perto)
        distancia_percorrida += matriz[atual][cidade_mais_perto]
        print(f" dist {distancia_percorrida} {atual} {cidade_mais_perto}")
        atual = cidade_mais_perto

    rota.append(rota[0])
    distancia_percorrida += matriz[atual][rota[0]]
    return (rota,round(distancia_percorrida * 111.11,5))
        
def main(path):
    relatorio = []
    matriz = get_matrix(path)
    print(matriz[32][51])
    for i in range(len(matriz)):
        relatorio.append(caixeiro(matriz,i))
    for rota in relatorio:
        print(rota[1])


main(path)



