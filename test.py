def criar_tabela_distribuicao(dados, num_classes):
    # Calcular a amplitude total dos dados
    amplitude = max(dados) - min(dados)

    # Calcular a largura das classes
    largura_classe = amplitude // num_classes

    # Inicializar o ponto de partida para a primeira classe
    ponto_partida = min(dados)

    # Inicializar um dicionário para armazenar as frequências das classes
    tabela = {}

    # Criar as classes e contar a frequência de cada classe
    for i in range(num_classes):
        classe = f'{ponto_partida}-{ponto_partida + largura_classe}'
        tabela[classe] = 0
        
        for dado in dados:
            if ponto_partida <= dado < ponto_partida + largura_classe:
                tabela[classe] += 1
        
        ponto_partida += largura_classe + 1  # Incrementar ponto de partida para a próxima classe

    return tabela

# Exemplo de uso
dados = [18, 22, 25, 27, 30, 32, 35, 38, 40, 45, 48, 52, 55, 60, 65]
num_classes = 5

tabela = criar_tabela_distribuicao(dados, num_classes)

# Imprimir a tabela de distribuição de frequência
print("| Classe  | Frequência |")
print("|---------|------------|")
for classe, frequencia in tabela.items():
    print(f"| {classe} |     {frequencia}     |")
