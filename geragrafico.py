import time
import timeit
import matplotlib.pyplot as plt
import mergesort
import vetoraleatorio
import bubblesort

vet1 =[]
vet2 =[]
vet3 =[]

def main(bubble):
    tamanho=1
    if(bubble == True):
        ran = 6
        mult = 5      
    else:
        ran = 11
        mult = 4 
    for x in range(ran):

        inicio=0
        fim=10000
        vet1.append(tamanho)

        vetor = vetoraleatorio.main(inicio, fim, tamanho)
        
        ini = time.time()
        mergesort.main(vetor)
        tempo = (time.time() - ini)
        vet2.append(round(tempo, 6))

        if(bubble == True):
            ini2 = time.time()
            bubblesort.main(vetor)
            tempo = (time.time() - ini2)
            vet3.append(round(tempo, 6))

        # print("tempo de execução: %.6f segundos " % tempo)
        tamanho = tamanho * mult

    #  [1,2,3,4,5]
    #  [0,50000,100000,150000,200000,250000]
    plt.plot(vet1,vet2,label='mergesort')
    if(bubble == True):
        plt.plot(vet1,vet3,label='bubblesort')
    plt.grid(True)
    plt.ylabel('tempo (s)')
    plt.xlabel('vetor')
    plt.title('Grafico tempo x tamanho')
    plt.legend()
    plt.show()