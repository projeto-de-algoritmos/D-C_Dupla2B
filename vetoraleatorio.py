from random import randint # para gerar os nums aleatorios
vetor = []

def vetorAleatorio(inicio, fim, tamanho):
    
    for i in range(tamanho): # vamos fazer isto tam (N) vezes
        vetor.append(randint(inicio, fim)) # gerar numero aleatorio entre L e H, e colocar na nossa lista
    #print("antes de ordenar\n",vetor)
    return vetor