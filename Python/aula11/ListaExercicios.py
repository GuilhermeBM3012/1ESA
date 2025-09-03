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
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def diagonal(matriz):
    for i in range(len(diagonal)):
        diagonal[i][i] = 1
    return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)


# 4 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - i - 1] = 1
    return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)

# 5 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def triangulo(matriz):
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz[0])):
            matriz[i][j] = 1
            matriz[j][i] = 2
        return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)

# 6 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def matriz_transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)

# 7 -


# 8 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def xadrez(matriz):
    for i in range(len(xadrez)):
        for j in range(len(xadrez[0])):
            if i % 2 == j % 2:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
    return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)


# 9 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def circulo(matriz):
    circulo = criaMatriz(1000, 1000)
    raio = len(circulo)/2
    for i in range(len(circulo)):
        for j in range(len(circulo[0])):
            if (i - raio)**2 + (j - raio)**2 <= raio**2:
                circulo[i][j] = 1
            else:
                circulo[i][j] = 0
    return

matriz = criar_matriz(50, 50)
diagonal(matriz)
mostrar_matriz(matriz)

# 10 -
def mostrar_matriz(matriz):
    for linhas in matriz:
        print(linhas)
    return

def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def xadrez(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i % 2 == j % 2:
                matriz[i][j] = 'vaga'
            else:
                matriz[i][j] = 'ocupada'
    return

matriz = criar_matriz(50, 50)
xadrez(matriz)
mostrar_matriz(matriz)

