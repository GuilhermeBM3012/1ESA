# QUANTAS VOGAIS TEM EM UM NOME:
vogais = 0
for nome in 'guilherme':
    if nome == 'a' or nome == 'e' or nome == 'i' or nome == 'o' or nome == 'u':
        vogais += 1

#     OU
vogais = 0
for nome in 'guilherme':
    if nome in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
print(vogais)

# -------------------------------------------------------------------------------
# QUANTOS PARES TEM EM 10 Nº DIGITADOS:
pares = 0
for i in range(10):  # 11 pq ele conta um a menos
    num = int(input('Diga um numero: '))
    if num % 2 == 0:
        pares += 1
print(f'Vc escreveu {pares} nº pares! ')

# ------------------------------------------------------------------------------
# CONTANDO DE 1 ATÉ 10:
for i in range(11):
    print(i)

# ------------------------------------------------------------------------------
# CONTANDO DE 1 ATÉ 10, PULANDO 2:
for i in range(1, 11, 2):  # vai do 1 ao 10, pulando 2
    print(i)

# ------------------------------------------------------------------------------
# CONTANDO DE 20 ATÉ 0, PULANDO 2:
for i in range(20, 0, -2):
    print(i)

# ------------------------------------------------------------------------------
# FIBONACCI
a = 1
b = 1
num = int(input('qt? '))
for i in range(num):
    c = a + b
    a = b
    b = c
    print(i)

# ------------------------------------------------------------------------------
# TABUADA
for i in range(1, 11):
    print(f'Tabuada do {i}:')
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
    print()

# ------------------------------------------------------------------------------
# PRINTANDO OS ELEMNTOS DE UMA LISTA:
lista = [3, True, 1.5, 'guilherme', []]
for elem in lista:
    print(elem)
    print(lista[0])
    print(lista[1])
    print(lista[2])
    print(lista[3])
    print(lista[4])

#     OU
lista = [3, True, 1.5, 'guilherme', []]
for i in range(len(lista)):
    print(f'Lista[{i}] = {lista[i]}')

# ------------------------------------------------------------------------------
# ALTERANDO UM ITEM DA LISTA:
lista = [3, True, 1.5, 'guilherme', []]
for i in range(len(lista)):
    lista[i] = 1
    print(f'Lista[{i}] = {lista[i]}')

# ------------------------------------------------------------------------------
# RELACIONANDO DUAS LISTAS:
profs = ['Danilo', 'Maluf', 'Gabi', 'Celso', 'Yan', 'Lucas', 'Luís']
materias = ['Python', 'Storytelling', 'Sw&TX', 'Cálculo', 'Arduino', 'Front-end', 'WebDev']
for i in range(len(profs)):
    print(f'O/A {profs[i]} dá {materias[i]}')

# ------------------------------------------------------------------------------
alunos = ['Lucas Sena', 'Rhariel', 'Guilherme', 'Luigi', 'Leandro']
notas = [4.5, 8.5, 10, 5, 7]
for i in range(len(alunos)):
    if notas[i] <= 6:
        print(f'{alunos[i]} = {notas[i]}: Reprovado!! ')
    else:
        print(f'{alunos[i]} = {notas[i]}: Aprovado!! ')

# ------------------------------------------------------------------------------
numeros = [9, 7, 3, 5, 2, 1, 8, 6, 0, 4]
pares = media = soma = 0
for num in numeros:  # VER QUANTOS PARES TEM
    if num % 2 == 0:
        pares += 1
for num in numeros:  # CALCULAR A SOMA
    soma += num
media = soma / len(numeros)
print(f'Vc digitou {pares} nº pares, sua soma é {soma} e sua média é {media}')

# POR ÍNDICE:
numeros = [9, 7, 3, 5, 2, 1, 8, 6, 0, 4]
pares = media = soma = 0
for i in range(len(numeros)):  # VER QUANTOS PARES TEM
    if numeros[i] % 2 == 0:
        pares += 1
for i in range(len(numeros)):  # CALCULAR A SOMA
    soma += numeros[i]
media = soma / len(numeros)  # CALCULANDO A MÉDIA
print(f'Vc digitou {pares} nº pares, sua soma é {soma} e sua média é {media}')

# ------------------------------------------------------------------------------
# ADICIONANDO UM ITEM A UMA LISTA VAZIA:
lista = []
lista.append(349)  # o append() add um item ao fim da lista
lista.append(67)
lista.append(765)
print(lista)

# ------------------------------------------------------------------------------
# EX (PEDIR 10 NUMEROS E ADD NA LISTA):
# COM WHILE
lista = []
i = 0
while i <= 10:
    num = input(f'Diga o {i+1}º numero: ')
    if not num.isnumeric():
        num = input('Diga um numero: ')
        continue
    num = int(num)
    lista.append(num)
    i += 1
print(lista)

# COM FOR
lista = []
for i in range(10):
    num = input(f'Diga o {i+1}º numero: ')
    while not num.isnumeric():
        num = input('Diga o {i+1}º numero: ')
        continue
    num = int(num)
    lista.append(num)
print(lista)

# ------------------------------------------------------------------------------
# VENDO QUEM É O MAIOR DA LISTA:
lista = [7, 3, 8, 5, 2, 1, 9, 6, 10, 4]
maior = lista[0]
for num in lista:
    print(f'Vou testar se {num} > {maior} ')
    if num > maior:
        print(f'Deu certo, vou trocar {maior} por {num} ')
        maior = num
print(f'O maior nº em {lista} é {maior} ')

# ------------------------------------------------------------------------------
# VENDO A POSÇÃO DO MAIOR Nº DA LISTA:
preco = [600, 50, 80, 1000000, 5]
carros = ['Mustang', 'Up', 'Gol', 'Polinho turbão manual', 'Uno']
indiceMaior = 0
maior = preco[0]
for i in range(len(preco)):
    print(f'Vou testar se {preco[i]} > {maior} ')
    if preco[i] > maior:
        print(f'Deu certo, vou trocar {maior} por {preco[i]} ')
        maior = preco[i]
        indiceMaior = i
print(f'O carro mais caro é o {carros[indiceMaior]}')
