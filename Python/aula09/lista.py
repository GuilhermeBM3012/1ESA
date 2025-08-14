# REVISÃO

# LISTAS

lista = [3, 'guilherme', 0.5, True]
for i in range (len(lista)):
    print(f'Lista[{i}] = {lista[i]}')

print('---------------------------------------------------')

lista = [3, 'guilherme', 0.5, True]
for elem in lista:
    print(elem)

print('---------------------------------------------------')

lista = [3, 'guilherme', 0.5, True]
for elem in lista:
    elem = 1
print(lista)

print('---------------------------------------------------')

lista = [3, 'guilherme', 0.5, True]
for i in range(len(lista)):
    lista[i] = 1
print(lista)

print('---------------------------------------------------')

lista = [4, 1, 5, 7, 3, 6, 9, 2, 10, 8]
soma = media = 0
for num in lista:
    soma += num
media = soma / len(lista)
print(f'A soma da lista é {soma} e a media é {media:.2f}')

#OU

lista = [4, 1, 5, 7, 3, 6, 9, 2, 10, 8]
soma = media = 0
for i in range(len(lista)):
    soma += lista[i]
media = soma / len(lista)
print(f'A soma da lista é {soma} e a media é {media:.2f}')

print('---------------------------------------------------')

lista = []
print(lista)
lista.append(1)
print(lista)

print('---------------------------------------------------')

lista = []
pares = impares = 0
for i in range(10):
    num = input(f'Diga o {i + 1}º nº: ')
    while not num.isnumeric():
        num = input(f'Diga o {i + 1}º nº: ')
    num = int(num)
    lista.append(num)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'\nDa lista {lista}'
      f'\nTem {pares} nº pares e {impares} nº impares')
