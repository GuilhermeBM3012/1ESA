# 1: 2 VALORES E INDICAR O MAIOR
n = int(input('Diga um valor: '))
n1 = int(input('Diga outro: '))
if n > n1:
    print(f'O maior número é {n} e o menor é {n1}')
elif n1 > n:
    print(f'O maior número é {n1} e o menor é {n}')
else:
    print('Os números tem que ser diferentes, TENTE NOVAMENTE!!! ')

print('---------------------------------')

# 2: PODE VOTAR?
a = int(input('Diga o ano que vc nasceu: '))
idade = 2025 - a
if idade < 16:
    print('Espere mais um puco para votar')
elif idade < 18 or idade >= 70:
    print('Pode votar, mas é opcional')
else:
    print('Vc tem que votar (obrigatório) ')

print('--------------------------------------------')

# 3: VERIFICAÇÃO DE SENHA
senha = input('Diga uma senha: ')
senhacerta = '1234'
if senha == senhacerta:
    print('ACESSO PERMITIDO ')
else:
    print('ACESSO NEGADO ')

print('-------------------------------------------')

# 4: PREÇO MAÇAS
m = int(input('Quantas maças vc comprou? '))
if m < 12:
    v = m * 0.3
    print(f'O valor a ser pago é R${v:.2f}')
else:
    v = m * 0.25
    print(f'O valor a ser pago é R${v:.2f}')

#              SEGUNDA MANEIRA

m = int(input('Quantas maças vc comprou? '))
if m < 12:
    v = 0.3
else:
    v = 0.25
total = m * v
print(f'Você vai pagar po maça {v} e o total é R${total:.2f}')


print('-----------------------------------------------')

# 5: ORDEM CRESCENTE
n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor valor: '))
n2 = int(input('Diga o terceiro valor: '))
if (n > n1) and (n1 > n2):
    print(f'A ordem crescente é: {n2}, {n1}, {n}')
elif (n > n2) and (n2 > n1):
    print(f'A ordem crescente é: {n1}, {n2}, {n}')
elif (n1 > n) and (n > n2):
    print(f'A ordem crescente é: {n2}, {n}, {n1}')
elif (n1 > n2) and (n2 > n):
    print(f'A ordem crescente é: {n}, {n2}, {n1}')
elif (n2 > n) and (n > n1):
    print(f'A ordem crescente é: {n1}, {n}, {n2}')
else:
    print(f'A ordem crescente é: {n}, {n1}, {n2}')

#              SEGUNDA MANEIRA

n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor valor: '))
n2 = int(input('Diga o terceiro valor: '))
if (n > n1) and (n > n2):
    aux = n
    n = n2
    n2 = aux
elif n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
if n1 < n:
    aux = n
    n = n2
    n2 = aux
print(n, n1, n2)

print('------------------------------------------------')

# 6: PESO IDEAL
s = str(input('Diga o seu sexo [M/F - m/f]: '))
a = float(input('Diga a sua altura [m]: '))
if s == 'M' or 'm':
    peso = (72.7 * a) - 58
    print(f'O seu peso ideal é {peso:.2f}kg')
else:
    peso = (62.1 * a) - 44.7
    print(f'O seu peso ideal é {peso:.2f}kg')

#              SEGUNDA MANEIRA

s = str(input('Diga o seu sexo [M/F - m/f]: '))
a = float(input('Diga a sua altura [m]: '))
if s == 'M' or 'm':
    peso = 72.7 * a - 58
else:
    peso = 62.1 * a - 44.7
print(f'O seu peso ideal é {peso:.2f}')

print('---------------------------------------------')

# 7/8: FORMA E SEU PERIMETRO
lados = int(input('Quantos lados tem a sua forma? '))
m = int(input('Diga qual é a medida do lado: '))
if lados < 3:
    print('Essa forma não é um polígono!!! ')
elif lados == 3:
    p = lados * m
    print(f'Sua forma é um Triângulo e seu perimetro vale {p}cm')
elif lados == 4:
    p = lados * m
    print(f'Sua forma é um Quadrado e seu perimetro vale {p}cm')
elif lados == 5:
    p = lados * m
    print(f'Sua forma é um Pentágono e seu perimetro vale {p}cm')
else:
    print('Polígono não encontrado!!! ')

#              SEGUNDA MANEIRA

lados = int(input('Quantos lados tem a sua forma? '))
if lados < 3:
    print('Essa forma não é um polígono!!! ')
elif lados > 5:
    print('Polígono não encontrado!!! ')
else:
    m = int(input('Diga qual é a medida do lado: '))
    p = lados * m
    if lados == 3:
        forma = 'Triângulo'
    elif lados == 4:
        forma = 'Quadrado'
    else:
        forma = 'Pentágono'
    print(f'Sua forma é {forma} e seu perimetro vale {p}')

print('----------------------------------------------------------')

# 9: 3 VALORES E INDICAR O MAIOR
n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor: '))
n2 = int(input('Diga o terceiro valor: '))
if (n > n1) and (n > n2):
    print(f'O maior número é {n}')
elif n1 > n2:  # tirou pq o n e n1 já foram comparados
    print(f'O maior número é {n1}')
else:
    print(f'O maior valor é {n2}')

#              SEGUNDA MANEIRA

n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor: '))
n2 = int(input('Diga o terceiro valor: '))
maior = n
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
print(maior)

print('-----------------------------------------------------------')

# 10: IDENTIFICAR O TRIÂNGULO PELOS LADOS
n = int(input('Diga o primeiro lado: '))
n1 = int(input('Diga o segundo lado: '))
n2 = int(input('Diga o terceiro lado: '))
if n2 == n1 and n == n2:  # NAO FAZER n == n1 == n2
    print('Seu triângulo é equilátero!!! ')
elif n == n1 != n2 or n != n1 == n2 or n1 != n == n2:
    print('Seu triângulo é isóceles!!! ')
else:
    print('Seu triângulo é escaleno!!! ')

print('------------------------------------------------------')

# 11: CLASSIFICANDO O TRIÂNGULO DE ACORDO COM OS ÂNGULOS
n = int(input('Diga o primeiro ângulo: '))
n1 = int(input('Diga o segundo ângulo: '))
n2 = int(input('Diga o terceiro ângulo: '))
if n + n1 + n2 == 180:
    if n == 90 or n1 == 90 or n2 == 90:
        print('Seu triângulo é retângulo!!! ')
    elif n > 90 or n1 > 90 or n2 > 90:
        print('Seu triângulo é obtusângulo!!! ')
    else:
        print('Seu triângulo é acutângulo!!! ')
else:
    print('Isso não é um triângulo!!! ')
