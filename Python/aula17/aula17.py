# ORDENANDO UMA LISTA COM 8 NUMS (SELECTION SORT)
def acha_menor(lista):
    indiceMenor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indiceMenor]:
            indiceMenor = i
    return indiceMenor

def selectionSort(lista):
    for i in range(len(lista)):
        localMenor = acha_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[localMenor]
        lista[localMenor] = aux
        print(lista)
    return lista

lista = [5, 0, 4, 1, 2, 7, 6, 3]
ordenada = selectionSort(lista)
print(ordenada)

print('---'*40)

# ORDENANDO UMA LISTA COM 8 NUMS (BUBBLE SORT)
def bubbleSort(lista):
    for j in range(len(lista)):
        contadorTrocas = 0
        for i in range(len(lista) - j - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                contadorTrocas += 1
                print(lista)
        if contadorTrocas == 0:
            break
    return lista

lista = [5, 0, 4, 1, 2, 7, 6, 3]
ordenada = bubbleSort(lista)
print(ordenada)

print('---'*40)

# BUSCA BINÁRIA PELA RAIZ QUADRADA DE UM Nº
def raizQuadrada(num):
    inicio = 0
    fim = num
    while fim - inicio > 0.001:
        chute = (inicio + fim)/2
        if chute **2 > num:
            fim = chute
        else:
            inicio = chute
        print(chute)
    return chute

x = raizQuadrada(25)
print(f'A raiz é: {x:.2f}')

print('---'*40)

# FUNÇÃO RECURSIVA DA DEF raizQuadrada
def raizQuadrada_recursiva(num, inicio = 0, fim = 0):
    if fim == 0:
        fim = num
    chute = (inicio + fim) / 2
    if fim - inicio > 0.001:
        if chute ** 2 > num:
            fim = chute
        else:
            inicio = chute
        chute = raizQuadrada_recursiva(num, inicio, fim)
    return chute

x = raizQuadrada_recursiva(25)
print(f'A raiz é: {x:.2f}')

print('---'*40)

# FUNÇÃO FORCA OPÇÕES PARA FAZER A RECURSIVA DPS
def forca_opcao(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n->'
    opcoes = input(msg)
    while opcoes not in listaOpcoes:
        opcoes = input(msg)
    return opcoes

print('---'*40)

# FUNCAO RECURSIVA DA DEF forca_opcao
def forca_opcao_recursiva(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n->'
    opcoes = input(msg)
    if opcoes not in listaOpcoes:
        opcoes = forca_opcao_recursiva(msg, listaOpcoes)
    return opcoes
