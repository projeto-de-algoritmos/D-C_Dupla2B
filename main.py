import geragrafico

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Mostra grafico mergesort")
    print("2. Mostra grafico comparando mergesort e bublesort") 
    print("3. Sair")
    print(67 * "-")


if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-3]: ")            
        if choice=='1':
            print("Opcao 1 foi escolhida")
            geragrafico.main(False)
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            geragrafico.main(True)
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
