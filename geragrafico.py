import time
import timeit
import matplotlib.pyplot as plt
import mergesort
import vetoraleatorio

vet1 =[]
vet2 =[]

def main():
    tamanho=1

    for x in range(10):

        inicio=0
        fim=10000
        vet1.append(tamanho)

        vetor = vetoraleatorio.main(inicio, fim, tamanho)
        
        ini = time.time()
        mergesort.main(vetor)
        tempo = (time.time() - ini)
        vet2.append(round(tempo, 6))

        # print("tempo de execução: %.6f segundos " % tempo)
        tamanho = tamanho * 4

    plt.plot(vet1,vet2)
    plt.show()