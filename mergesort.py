
def main(vet):
    
    #print("Splitting ",vet)
    if len(vet)>1:
        mid = len(vet)//2
        lefthalf = vet[:mid]
        righthalf = vet[mid:]

        main(lefthalf)
        main(righthalf)

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