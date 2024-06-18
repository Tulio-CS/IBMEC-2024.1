
lista_tempos = [10,5,6,7,20]



def calcula_atraso(atual,esperado):
    return (atual-esperado)

for i in range(len(lista_tempos)):
    atraso = calcula_atraso(lista_tempos[i],5)

    if atraso > 0 :
        print(f"O projeto {i} atraso e de {atraso}")
    elif atraso == 0:
        print("Não há atraso")
    else:
        print(f"O projeto {i} esta adiantado em {-atraso}")
