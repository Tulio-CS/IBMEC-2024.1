
distancias = [[0,1.6114,0.9848,1.3158],
              [1.6114,0,0.8841,0.6142],
              [0.9848,0.8841,0,0.3612],
              [1.3158,0.6142,0.3612,0]]

cidades = {0:"belo horizonte",1:"lagoa da prata",2:"claudio",3:"itapecerica"}
def caixeiro(matriz_distancias):
    caminho=[0]*len(matriz_distancias)
    distancia_percorrida=0
    inicio = int(input("Qual cidade você vai começar o percurso ?\n0 - Belo Horizonte\n1 - Lagoa da Prata\n2 - Claudio\n3 - Itapecerica\n"))
    caminho[inicio] = 1
    rota = [inicio]
    atual = inicio
    for i in range(1,4):
        Menor=float("inf")
        cidade_mais_perto=None
        for j in range(4):
            if matriz_distancias[atual][j] < Menor and caminho[j] == 0:
                cidade_mais_perto = j
                Menor = distancias[atual][j]

        caminho[cidade_mais_perto] = i
        rota.append(cidade_mais_perto)
        distancia_percorrida += distancias[atual][cidade_mais_perto]
        atual = cidade_mais_perto

    rota.append(rota[0])
    distancia_percorrida += distancias[atual][rota[0]]
    return (rota,distancia_percorrida)


if __name__ == "__main__":
    rota = caixeiro(distancias)
    print("\nA melhor rota é :\n")
    for cidade in rota[0]:
        print(cidades[cidade])
    print("\nA distancia percorrida será : {}Km".format(round(rota[1]*111.11,2)))