# 1 -
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f'matriz[{i}][{j}] = {matriz[i][j]}')


# 2 -
def mostraMatriz(matriz):
    for linha in matriz:
        print(linha)
    return

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(i)  # se for (i) a 1º linha so vai ser 0, a 2º 1 e assim por diante, pq o i é constante
        matriz.append(linha)  # se for (i+j) as coress ficam na diagonal
    return matriz


# 3 -
for i in range(len(diagonal)):
    diagonal[i][i] = 1


# 4 -
for i in range(len(matriz)):
    matriz[i][len(matriz) - i - 1] = 1


# 5 -


# 6 -


# 7 -


# 8 -
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i % 2 == j % 2:
            xadrez[i][j] = 0
        else:
            xadrez[i][j] = 1


# 9 -
circulo = criaMatriz(1000, 1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i - raio)**2 + (j - raio)**2 <= raio**2:
            circulo[i][j] = 1
        else:
            circulo[i][j] = 0


# 10 -


