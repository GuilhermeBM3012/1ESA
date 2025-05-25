# PERGUNTA QUANTOS NUMEROS QUER COLOCAR NA LISTA, DPS PEDE OS NUMEROS E
# DPS ADICIONA ELES NO FINAL DA LISTA:
qntdNum = input('Diga quantos numeros vc quer inserir: ')
while not qntdNum.isnumeric():
    qntdNum = input('Diga quantos numeros vc quer inserir: ')
qntdNum = int(qntdNum)

lista = []
while len(lista) < qntdNum:
    num = input(f'Diga o {len(lista) +1}º numero: ')
    while not num.isnumeric():
        num = input(f'Diga o {len(lista) +1}º numero: ')
    num = int(num)
    lista.append(num)
print(lista)

# COM FUNCTION:

def verificaNum(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

qntd = verificaNum('Diga quantos numeros vc quer inserir: ')

lista = []
while len(lista) < qntd:
    num = verificaNum(f'Diga o {len(lista) + 1}º numero: ')
    lista.append(num)
print(lista)

# -------------------------------------------------------------------
# OBRIGANDO A DIGITAR UM VINHO:
def forcaOpcao(msg, listaOpcao):
    opcoes = '\n'.join(listaOpcao)  # junta as strings da lista em uma string só
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in listaOpcao:  # (escolha == 'Pérgola' or escolha == 'Sangue de boi' or escolha == 'Salton')
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

vinhos = ['Pérgola', 'Sangue de boi', 'Salton']
vinho = forcaOpcao('Qual vinho vc quer?', vinhos)
print(f'Vc escolheu o {vinho}')

opcoes = ['s', 'n']
continuar = forcaOpcao('Vc quer continuar?', opcoes)
print(f'Vc escolheu {continuar}')

# -------------------------------------------------------------------
# CALCULA A MEDIA DOS NUMEROS DENTRO DE UMA LISTA:
def calculoMedia(listaNumeros):
    soma = 0
    for num in listaNumeros:
        soma += num
    media = soma / len(listaNumeros)
    return media

lista = [2, 5, 3, 7, 5, 9, 2, 12, 20, 10]
media = calculoMedia(lista)
print(f'{media:.2f}')
lista2 = [2, 5, 3, 7, 5]
media = calculoMedia(lista2)
print(f'{media:.2f}')

# -------------------------------------------------------------------
# VER QUANTOS PARES TEM EM UMA LISTA:
def qntdPares(listaNumeros):
    pares = 0
    for num in listaNumeros:
        if num % 2 == 0:
            pares += 1
    return pares

lista = [3, 6, 4, 8, 7, 6, 0, 2, 11]
pares = qntdPares(lista)
print(f'De todos os numeros da lista, tem {pares} nº pares')
lista2 = [10, 2, 5, 8, 3, 9, 0]
pares = qntdPares(lista2)
print(f'De todos os numeros da lista, tem {pares} nº pares')

# -------------------------------------------------------------------
# VER QUEM É O MAIOR ELEMNTO DA LISTA:
def verMaior(listaNumeros):
    indice_maior = 0
    maior = listaNumeros[indice_maior]
    for i in range(len(listaNumeros)):
        if listaNumeros[i] > maior:
            maior = listaNumeros[i]
            indice_maior = i
    return indice_maior

lista = [5, 2, 4, 5, 9, 1]
indice_maior = verMaior(lista)
print(f'O maior número é {lista[indice_maior]}')

lista2 = [7, 4, 8, 9, 1, 0, 10, 3]
indice_maior = verMaior(lista2)
print(f'O maior número é {lista2[indice_maior]}')

# -------------------------------------------------------------------
# MOSTRA A OPÇÃO DOS CARROS:
def join(lista_str, sep):
    ajuntado = lista_str[0]
    for i in range(len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado
def forcaOpcao(msg, listaOpcao):
    # opcoes = '\n'.join(listaOpcao)
    opcoes = join(listaOpcao, '\n')
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in listaOpcao:  # (escolha == 'Pérgola' or escolha == 'Sangue de boi' or escolha == 'Salton')
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

def acha_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = ['up', 'gol', 'polinho turbão manual', 'uno', 'celta']
precos = [10, 20, 1000000, 100, 200]

escolha = forcaOpcao('Qual carro vc deseja?', carros)
indiceEscolha = acha_index(carros, escolha)
print(f'O {escolha} custa {precos[indiceEscolha]}')
