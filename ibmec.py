from math import inf

#distancias = [[0,2,11,6,15,11,1], [2,0,7,12,4,2,15], [11,7,0,11,8,3,13], [6,12,11,0,10,2,1], [15,4,8,10,0,5,12], [11,2,3,2,5,14], [1,15,131,13,14,0]]
distancias =[[0,2,11,5,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,6,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]]

n_cidades = 7
visitadas = [False]*len(distancias[0])
caminho = []
a_visitar = [1,2,3,4]
atual = 5

for i in a_visitar:
    menor = inf
    prox = None
    for j in range(len(distancias[atual])):
        if distancias[atual][j] < menor and distancias[atual][j] != 0 and j in a_visitar and visitadas[j] == False:
            menor = distancias[atual][j]
            prox = j
    caminho.append(prox)
    visitadas[prox] = True
    atual = prox
        

    
print(caminho)


    


print(caminho)


