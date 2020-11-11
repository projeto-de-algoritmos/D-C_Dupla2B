import time
import timeit
import matplotlib.pyplot as plt

from random import randint # para gerar os nums aleatorios
vetor = []

def vetorAleatorio(inicio, fim, tamanho):
    
    for i in range(tamanho): # vamos fazer isto tam (N) vezes
        vetor.append(randint(inicio, fim)) # gerar numero aleatorio entre L e H, e colocar na nossa lista
    #print("antes de ordenar\n",vetor)
    return vetor


def mergeSort(vet):
    
    #print("Splitting ",vet)
    if len(vet)>1:
        mid = len(vet)//2
        lefthalf = vet[:mid]
        righthalf = vet[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                vet[k]=lefthalf[i]
                i=i+1
            else:
                vet[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            vet[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            vet[k]=righthalf[j]
            j=j+1
            k=k+1
   # print("Merging ",alist)


a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
vet1 =[]
vet2 =[]

tamanho=1
for x in range(10):
    inicio=0
    fim=10000
    vet1.append(tamanho)
    vetorAleatorio(inicio, fim, tamanho)
    ini = time.time()
    mergeSort(vetor)
    tempo = (time.time() - ini)
    vet2.append(round(tempo, 6))
    print("tempo de execução: %.6f segundos " % tempo)
    tamanho = tamanho * 4

plt.plot(vet1,vet2)
plt.show()