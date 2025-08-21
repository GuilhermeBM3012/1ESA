# BORRANDO UMA IMAGEM

# instalou o pacote: matplotlib
import matplotlib.pyplot as plt

# qtd de sub-listas diz a qtd de linhas e a qtd de itens dentro das sub-listas
# diz a qtd de colunas
matriz = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

plt.imshow(matriz, 'hot')  
plt.colorbar()  
plt.show()

matriz = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
print(matriz[0])
print(type(matriz[0]))
print(matriz[0][2])

# PRINTAR CADA ELEM DA LISTA MATRIZ
for sub_lista in matriz:
    for num in sub_lista:
        print(num)

# MLR JEITO
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f'matriz[{i}][{j}] = {matriz[i][j]}')


# FUNÇÃO P/ GERAR UMA MATRIZ AUTOMATICAMENTE
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

a = criaMatriz(50, 50)
mostraMatriz(a)
plt.imshow(a, 'hot')
plt.colorbar()
plt.show()

print('------------------------------------------------------------------')

# DIAGONAL DE UMA COR E O RESTO DE OUTRA
def mostraMatriz(matriz):
    for linha in matriz:
        print(linha)
    return

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

diagonal = criaMatriz(10, 10)
for i in range(len(diagonal)):
    diagonal[i][i] = 1
plt.imshow(diagonal, 'hot')
plt.colorbar()
plt.show()

print('------------------------------------------------------------------')

# TABULEIRO DE XADREZ
def mostraMatriz(matriz):
    for linha in matriz:
        print(linha)
    return

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
   
xadrez = criaMatriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i % 2 == 0:
            if j % 2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j % 2 != 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1

plt.imshow(xadrez, 'hot')
plt.colorbar()
plt.show()

print('------------------------------------------------------------------')

# CIRCULO
def mostraMatriz(matriz):
    for linha in matriz:
        print(linha)
    return

def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

circulo = criaMatriz(1000, 1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i - raio)**2 + (j - raio)**2 <= raio**2:
            circulo[i][j] = 1
        else:
            circulo[i][j] = 0

plt.imshow(circulo, 'hot')
plt.colorbar()
plt.show()