# --- SISTEMA DE ORDENAÇÃO ---

# ORDENANDO UMA LISTA COM 7 NUMS
def acha_menor(lista):
    indiceMenor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indiceMenor]:
            indiceMenor = i
    return indiceMenor

def ordenaLista(lista):
    listaOrdenada = []
    while lista:
        localMenor = acha_menor(lista)
        menor = lista.pop(localMenor)
        listaOrdenada.append(menor)
        print(lista)
        print(listaOrdenada)
    return listaOrdenada

listaNum = [3, 1, 5, 6, 2, 4, 7]
listaOrdenada = ordenaLista(listaNum)
print(listaOrdenada)

print('---'*40)

# MELHOR JETIO
def ordenaLista(lista):
    for i in range(len(lista)):
        localMenor = acha_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[localMenor]
        lista[localMenor] = aux
        print(lista)
    return lista
listaNum = [3, 1, 5, 6, 2, 4, 7]
ordenada = ordenaLista(listaNum)
print(ordenada)

print('---'*40)

# ACHAR A RAIZ QUADRADA DE UM NUM
def acha_raiz(num):
    while True:
        try:
            palpite = float(input(f'Diga qual é a raiz quadrada de {num}: \n--> '))
        except:
            print('Tem q ser float')
        else:
            pot = palpite ** 2
        if pot > num:
            print('O seu palpite tem q ser mais baixo')
        elif pot < num:
            print('Seu palpite tem q ser mais alto')
        else:
            print('Parabéns vc acertou!!! ')
            break
    return
raizQuadrada = acha_raiz(25)

# MELHOR JEITO