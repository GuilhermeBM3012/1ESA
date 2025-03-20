# 1
n = int(input('Diga um valor: '))
n1 = int(input('Diga outro: '))
if n > n1:
    print(f'O maior número é {n}')
else:
    print(f'O menor número é {n1}')

print('---------------------------------')

# 2
a = int(input('Diga o ano que vc nasceu: '))
votar = 2025 - a
if votar >= 18:
    print('Vc pode votar ')
else:
    print('Vc ainda não pode votar ')

print('--------------------------------------------')

# 3
senha = int(input('Diga uma senha: '))
senhacerta = 1234
if senha == senhacerta:
    print('ACESSO PERMITIDO ')
else:
    print('ACESSO NEGADO ')

print('-------------------------------------------')

# 4
m = int(input('Quantas maças vc comprou? '))
if m < 12:
    v = m * 0.3
    print(f'O valor a ser pago é {v}')
else:
    v = m * 0.25
    print(f'O valor a ser pago é {v}')

print('-----------------------------------------------')

# 6
s = str(input('Diga o seu sexo [M/F - m/f]: '))
a = float(input('Diga a sua altura [m]: '))
if s == 'M' or 'm':
    peso = (72.7 * a) - 58
    print(f'O seu peso ideal é {peso:.2f}kg')
else:
    peso = (62.1 * a) - 44.7
    print(f'O seu peso ideal é {peso:.2f}kg')

print('---------------------------------------------')

# 7
lados = int(input('Quantos lados tem a sua forma? '))
m = int(input('Diga qual é a medida do primeiro lado: '))
m1 = int(input('Diga qual é a medida do segundo lado: '))
if lados == 3:
    a = (m * m1) / 2
    print(f'Sua forma é um Triângulo e sua área vale {a}cm2')
elif lados == 4:
    a = m * m1
    print(f'Sua forma é um Quadrado e sua área vale {a}cm2')
else:
    a = (5 * m * m1) / 2
    print(f'Sua forma é um Pentágono e sua área vale {a}cm2') 
