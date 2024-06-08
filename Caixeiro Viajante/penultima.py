distancias = [[0,1.6114,0.9848,1.3158],
              [1.6114,0,0.8841,0.6142],
              [0.9848,0.8841,0,0.3612],
              [1.3158,0.6142,0.3612,0]]

cidades = {0:"belo horizonte",1:"lagoa da prata",2:"claudio",3:"itapecerica"}

def caixeiro():
    caminho = [None] * len(distancias)
    atual = None


    while True: 
        inicio = input("Qual cidade você vai começar o percurso ?\n1 - Belo Horizonte\n2 - Lagoa da Prata\n3 - Claudio\n4 - Itapecerica\n")
        if inicio in "1234" and len(inicio) == 1:
            inicio = int(inicio) - 1
            caminho[0] = inicio
            atual = inicio
            break
        else:
            print("entrada invalida!\n")

    while True:
            penultima = input("Você quer definir uma cidade para ser a penultima ?\n1 - Sim\n2 - Não\n")
            if penultima in "12" and len(penultima) == 1:
                if int(penultima) == 2:
                    break
                else:
                    penultima = input("Qual a penultima cidade ?\n1 - Belo Horizonte\n2 - Lagoa da Prata\n3 - Claudio\n4 - Itapecerica\n")
                    if penultima in "1234" and len(penultima) == 1 and int(penultima) != inicio:
                        penultima = int(penultima) - 1
                        caminho[2] = penultima
                        break
                    else:
                        print("Entrada invalida!\n")
            else:
                print("Entrada Invalida!\n")


    for i in range(len(caminho)-1):
        menor = float("inf")
        if caminho[i+1] == None:
            for j in range(len(distancias[i])):
                if distancias[atual][j] < menor and distancias[atual][j] != 0 and j not in caminho:
                    menor = j
            caminho[caminho.index(None)] = menor
            atual = menor
    return caminho


if __name__ == "__main__":
    caminho = caixeiro()
    print("\nO caminho é:\n")
    for rota in caminho:
        print(cidades[rota])



