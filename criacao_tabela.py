from valores import *
from tabulate import *

def criar_tabela():
    classes, amplitude, dados = variaveis()
    ask = input("Deseja imprimir os dados (sim/nao): ")
    if ask.upper() == "SIM" or ask.upper() == "S":
        print("dados: ", dados)

    limite_min = min(dados)
    tabela = {}

    for i in range(classes):
        classe = f'{limite_min}-{limite_min + amplitude - 1}'
        tabela[classe] = 0

        for dado in dados:
            if dado >= limite_min and dado <= limite_min + amplitude - 1:
                tabela[classe] += 1

        limite_min += amplitude
    
    distro = [[classe, frequencia] for classe, frequencia in tabela.items()]
    print(tabulate(distro, headers=["Classes", "Frequencia"], tablefmt="grid",stralign="center", numalign="center"))
