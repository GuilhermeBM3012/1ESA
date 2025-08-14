# LISTA DE WHILE
# 2 - 3 - 6 - 7 - 12 - 14 - 15

# 2
nome = input('Diga seu nome: ')
while not len(nome) >= 3:
    nome = input('Diga seu nome: ')

while True:
    idade = input('Diga sua idade [0-150]:')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade <= 150:
            break
        else:
            print('Tem q ser um nº! ')

while True:
    salario = input('Diga seu salario:')
    while not salario.isdecimal():
        salario = input('Diga seu salario:')
    salario = float(salario)
    break

sexo = input('Diga seu sexo [f / m]:')
while sexo != 'f' and sexo != 'm':
    sexo = input('Diga seu sexo [f / m]:')

estadoCivil = input('Diga seu estado civil [s / c / v / d]:')
while not (estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd'):
    estadoCivil = input('Diga seu estado civil [s / c / v / d]:')

# 3
popA = 80
popB = 20
totAno = 0
while popA == popB:
    popA += 3/100 / 100
    popB *= 1.015
    totAno += 1
print(f'Demorou {totAno} anos p/ a populaça de A se igualar a de B! ')

# 6
while True:
    nomeUsuario = input('Diga seu nome de usuario: ')
    senha = input('Diga sua senha: ')
    while nomeUsuario == senha:
        print('N o nome de usuario n pode ser igual a senha!')
        nomeUsuario = input('Diga seu nome de usuario: ')
        senha = input('Diga sua senha: ')
    if nomeUsuario != senha:
        print('Login feito!')
        break

# 7
num = input('Diga um nº para a tabuada:')
while not num.isnumeric():
    num = input('Diga um nº para a tabuada:')
num = int(num)
cont = 0
while cont <= 10:
    print(f'{num} X {cont} = {num*cont}')
    cont += 1
# COM FOR
for i in range(11):
    print(f'Tabuada do {i}')
    for j in range(11):
        print(f'{i} x {j} = {i * j}')

# 12
qtdNum = input('Quantos nº vq quer somar e ver a media? ')
while not qtdNum.isnumeric():
    qtdNum = input('Quantos nº vq quer somar e ver a media? ')
qtdNum = int(qtdNum)
cont = 0
soma = 0
while cont < qtdNum:
    num = input(f'Diga o {cont + 1} nº:')
    while not num.isnumeric():
        num = input(f'Diga o {cont + 1} nº:')
    num = int(num)
    soma += num
    cont += 1
media = soma / qtdNum
print(f'Vc digitou {qtdNum} nº - sua soma é: {soma} e a media é: {media:.2f} ')

# 14

# 15


