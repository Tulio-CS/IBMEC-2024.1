import pandas as pd
from math import sqrt
import folium



def distancia_euclidiana(p1,p2):
    return sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def get_sheet(path):
    xlsx = pd.ExcelFile(path)
    for i , sheet in enumerate(xlsx.sheet_names):
        print("{} {}".format(i,sheet))
    pagina = int(input("Selecione um bairro para ser estudado :\n"))
    return xlsx.sheet_names[pagina]

def get_matrix(df,sheet):
    df = pd.read_excel(path,sheet_name=sheet)
    df_coords = df[['Latitude WGS84', 'Longitude WGS84']].dropna()
    matriz = [[0] * len(df) for i in range(len(df))]
    for i in range(len(df_coords)):
        for j in range(i+1,len(df_coords)):
            dist = distancia_euclidiana((df_coords.iloc[i]["Latitude WGS84"],df_coords.iloc[i]["Longitude WGS84"]),(df_coords.iloc[j]["Latitude WGS84"],df_coords.iloc[j]["Longitude WGS84"]))
            matriz[i][j] = dist
            matriz[j][i] = dist
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
        atual = cidade_mais_perto

    rota.append(rota[0])
    distancia_percorrida += matriz[atual][rota[0]]
    return (rota,round(distancia_percorrida * 111.11,5))
        
def main(path):
    relatorio = []
    sheet = get_sheet(path)
    matriz = get_matrix(path,sheet)
    excel = pd.read_excel(path,sheet_name=sheet)
    for i in range(len(matriz)):
        relatorio.append(caixeiro(matriz,i))
    min_dist = min([relatorio[i][1] for i in range(len(relatorio))])
    best_route = [relatorio[i][0] for i in range(len(relatorio)) if relatorio[i][1] == min_dist][0]
    points = [(excel.iloc[i]["Latitude WGS84"],excel.iloc[i]["Longitude WGS84"]) for i in best_route]
    
    mymap = folium.Map(location=points[0], zoom_start=5)

    for lat, long in points:
        folium.Marker(location=[lat, long]).add_to(mymap)
    folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(mymap)
    
    mymap.save(f"fio de cobre/mapas/{sheet}_{min_dist}km.html".replace(" - Telefonia",""))


if __name__ == "__main__":
    path = "fio de cobre\df.xlsx"
    main(path)







