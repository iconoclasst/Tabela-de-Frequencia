import sys
from math import ceil

def terminal(): #Função inserir valores por terminal
    print("Insira os valores ou Enter para sair")
    valores = []
    line = sys.stdin.readline()

    while line.split():
        print("Insira os valores ou Enter para sair")
        valores.extend(map(int, line.split()))
        line = sys.stdin.readline()
    return valores

def anexar(): #Função carregar arquivo contendo valores
    fileName = input("Caminho do arquivo: ")
    valores = []
    try:
        with open(fileName, 'r') as file:
            for line in file:
                valores.extend(map(int, line.split()))
    except FileNotFoundError:
        print("Arquivo não encontrado")
    return valores

def variaveis(): #Função definir variaveis de construção de tabela
    valores = opcao()
    k = int(input("Insira o numero de classes (5-10): "))
    h = ceil((max(valores) - min(valores) + 1) / k)
    return k, h, valores


def opcao():
    print("Opção 1: Inserir valores por terminal")
    print("Opção 2: Carregar valores por arquivo")

    opc = int(input())
    if opc == 1:
        return terminal()
    elif opc == 2:
        return anexar()
    



