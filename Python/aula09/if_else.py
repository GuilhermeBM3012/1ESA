# REVISÃO

# LISTA DE IF / ELSE
#4 - 5 - 6 - 7 - 8- 9

# 4
qtd = int(input('Quantas maças vc deseja? '))
if qtd < 12:
    valor = qtd * 0.3
valor = qtd * 0.25
print(f'Vc comprou {qtd} maças e gastou R${valor}')

# 5
n1 = int(input('Diga o 1º nº:'))
n2 = int(input('Diga o 2º nº:'))
n3 = int(input('Diga o 3º nº:'))
if n1 > n2:
    aux = n1  # AUX = MAIOR
    n1 = n2
    n2 = aux
    print(n1, n2, n3)
if n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
    print(n1, n2, n3)
if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
    print(n1, n2, n3)

# 6
sexo = input('Diga o seu sexo [f=1 / m=2]:')
altura = float(input('Diga a sua altura em m: '))
if sexo == '1':
    peso = (72.7 * altura) - 58
elif sexo == '2':
    peso = (62.1 * altura) - 44.7
else:
    print('Sexo n identificado! ')
print(f'O seu peso ideal é {peso}Kg')

# 7 / 8
lados = int(input('Diga a qtd de lados: '))
if lados < 3:
    print('N é um polígono')
elif lados > 5:
    print('Poligono n identificado')
else:
    medida = int(input('Diga a medida do lado: '))
    if lados == 3:
        print(f'É um triangulo')
    elif lados == 4:
        print(f'É um quadrado')
    else:
        print('É um pentagono')
    perimetro = lados * medida
    print(f'Seu perimetro é {perimetro} m')

# 9
n1 = int(input('Diga o 1º nº:'))
n2 = int(input('Diga o 2º nº:'))
n3 = int(input('Diga o 3º nº:'))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(maior)




