from random import randint # para gerar os nums aleatorios
vetor = []

def vetorAleatorio(inicio, fim, tamanho):
    
    for i in range(tamanho): # vamos fazer isto tam (N) vezes
        vetor.append(randint(inicio, fim)) # gerar numero aleatorio entre L e H, e colocar na nossa lista
    print("antes de ordenar\n",vetor)
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


#L = int(input('Informe o valor inteiro minimo da faixa:'))
#H = int(input('Informe o valor inteiro maximo da faixa:'))
#tam = int(input('Informe a quantidade de valores a serem sorteados:'))
inicio=0
fim=100
tamanho=50

vetorAleatorio(inicio, fim, tamanho)
mergeSort(vetor)
print(vetor)