# 1: 2 VALORES E INDICAR O MAIOR
n = int(input('Diga um valor: '))
n1 = int(input('Diga outro: '))
if n > n1:
    print(f'O maior número é {n}')
else:
    print(f'O menor número é {n1}')

print('---------------------------------')

# 2: PODE VOTAR?
a = int(input('Diga o ano que vc nasceu: '))
votar = 2025 - a
if votar >= 18:
    print('Vc pode votar ')
else:
    print('Vc ainda não pode votar ')

print('--------------------------------------------')

# 3: VERIFICAÇÃO DE SENHA
senha = int(input('Diga uma senha: '))
senhacerta = 1234
if senha == senhacerta:
    print('ACESSO PERMITIDO ')
else:
    print('ACESSO NEGADO ')

print('-------------------------------------------')

# 4: PREÇO MAÇAS
m = int(input('Quantas maças vc comprou? '))
if m < 12:
    v = m * 0.3
    print(f'O valor a ser pago é {v}')
else:
    v = m * 0.25
    print(f'O valor a ser pago é {v}')

print('-----------------------------------------------')

# 5: ORDEM CRESCENTE
n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor valor: '))
n2 = int(input('Diga o terceiro valor: '))
if n > n1 > n2:
    print(f'{n2}, {n1}, {n}')
elif n > n2 > n1:
    print(f'{n1}, {n2}, {n}')
elif n1 > n > n2:
    print(f'{n2}, {n}, {n1}')
elif n1 > n2 > n:
    print(f'{n}, {n2}, {n1}')
elif n2 > n > n1:
    print(f'{n1}, {n}, {n2}')
else:
    print(f'{n}, {n1}, {n2}')

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

print('---------------------------------------------')

# 7/8: FORMA E SUA ÁREA
lados = int(input('Quantos lados tem a sua forma? '))
m = int(input('Diga qual é a medida do primeiro lado: '))
m1 = int(input('Diga qual é a medida do segundo lado: '))
if lados == 3:
    a = (m * m1) / 2
    print(f'Sua forma é um Triângulo e sua área vale {a}cm2')
elif lados == 4:
    a = m * m1
    print(f'Sua forma é um Quadrado e sua área vale {a}cm2')
elif lados == 5:
    a = (5 * m * m1) / 2
    print(f'Sua forma é um Pentágono e sua área vale {a}cm2')
elif lados < 3:
    print('Essa forma não é um polígono!!! ')
else:
    print('Polígono não encontrado!!! ')

print('----------------------------------------------------------')

# 9: VALORES E INDICAR O MAIOR
n = int(input('Diga o primeiro valor: '))
n1 = int(input('Diga o segundo valor: '))
n2 = int(input('Diga o terceiro valor: '))
if (n > n1) and (n1 > n2):
    print(f'O maior número é {n}')
elif (n1 > n) and (n1 > n2):
    print(f'O menor número é {n1}')
else:
    print(f'O maior valor é {n2}')

print('-----------------------------------------------------------')

# 10: IDENTIFICAR O TRIÂNGULO PELOS LADOS
n = int(input('Diga o primeiro lado: '))
n1 = int(input('Diga o segundo lado: '))
n2 = int(input('Diga o terceiro lado: '))
if n == n1 == n2:
    print('Seu triângulo é equilátero!!! ')
elif n == n1 != n2:
    print('Seu triângulo é isóceles!!! ')
else:
    print('Seu triângulo é escaleno!!! ')

print('------------------------------------------------------')

# 11: CLASSIFICANDO O TRIÂNGULO DE ACORDO COM OS ÂNGULOS
n = int(input('Diga o primeiro ângulo: '))
n1 = int(input('Diga o segundo ângulo: '))
n2 = int(input('Diga o terceiro ângulo: '))
if n or n1 or n2 == 90:
    print('Seu triânguilo é retângulo!!! ')
elif n or n1 or n2 > 90:
    print('Seu triânguilo é obtusângulo!!! ')
else:
    print('Seu triânguilo é acutângulo!!! ')
