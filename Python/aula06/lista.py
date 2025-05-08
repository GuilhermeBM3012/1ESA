# 1 - TEM Q DIGITAR UM N° ENTRE 0 E 10
quant = 1
cont = 0
while cont < quant:
    nota = int(input('Diga uma nota entre 0 e 10: '))
    cont += 1
    if 0 <= nota <= 10:
        print('Nota válida!! ')
    else:
        print('Nota inválida ')

'''-------------------------------------------------------------------------'''
# 1 - CORREÇÃO
while True:
    num = input('Diga um numero: ')
    if num.isnumeric():
        num = int(num)
        if num > 0 and num <= 10:
            print('Numero valido! ')
            break

#         OU

n = input('Diga um valor ´para tabuada: ')
while not n.isnumeric():
    n = input('Diga um valor ´para tabuada: ')
n = int(n)
if n > 0 and n <= 10:
    print('Numero valido! ')

'''----------------------------------------------------------------------------'''
# 2 - VALIDAR ALGUMAS INFORMAÇÕES # IMPORTANTE!!!
nome = input('Diga seu nome: ')
idade: int(input('Diga sua idade: '))
salario = float(input('Diga o seu salário: '))
sexo = input('Diga seu sexo [m - f]: ').lower()
ec = input('Diga seu estado civil [s - c - v - d]: ').lower()
while not (len(nome) > 3 and 0 < idade >= 150 and salario > 0 and sexo == 'm' or sexo == 'f' and ec == 'c' or ec == 's' or ec == 'v' or ec == 'd'):
    print('Não validado! ')
    nome = input('Diga seu nome: ')
    idade: int(input('Diga sua idade: '))
    salario = float(input('Diga o seu salário: '))
    sexo = input('Diga seu sexo [m - f]: ').lower()
    ec = input('Diga seu estado civil [s - c - v - d]: ').lower()
print('Validado ! ')

'''----------------------------------------------------------------------------'''
# 2 - CORREÇÃO
nome = input('Diga seu nome: ')
while len(nome) < 3:
    nome = input('Diga seu nome: ')

while True:
    idade = input('Diga a sua idade: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade <= 150:
            break
    else:
        print('Deve digitar um numero')

salario = input('Diga seu salario: ')
while not salario.isnumeric():
    salario = input('Diga seu salario: ')
salario = int(salario)

sexo = input('Diga seu sexo [m - f]: ').lower()
while sexo != 'm' or sexo != 'f':
    sexo = input('Diga seu sexo [m - f]: ').lower()

ec = input('Diga seu estado civil [s - c - v - d]: ').lower()
while not ec == 'c' or ec == 's' or ec == 'v' or ec == 'd':
    ec = input('Diga seu estado civil [s - c - v - d]: ').lower()

'''----------------------------------------------------------------------------'''
# 3 - POPULACAO DE A CHEGAR EM B
# A = 80 * 1,03^T  ---  B = 200 * 1,015^T
a = 80
b = 200
t = 0
while a < b:
    a *= 1.03
    b *= 1.015
    t += 1
print(f'Para a populacao de A passar a de B, demorará {t} anos! c')

'''----------------------------------------------------------------------------'''
# 4 - SOMA E MEDIA DE 5 Nº
quant = 5
cont = 0
soma = 0
while cont < quant:
    n = int(input('Diga um numero: '))
    cont += 1
    soma += n
    media = soma / quant
print(f'A soma dos {quant} nº é {soma} e sua media é {media}')

'''----------------------------------------------------------------------------'''
# 4 - CORREÇÃO
cont = 0
soma = 0
while cont < 5:
    n = input(f'Diga a {cont + 1}º nota: ')
    while not n.isnumeric():
        n = input(f'Diga a {cont + 1}º nota: ')
    n = int(n)
    soma += n
    cont += 1
media = soma / 5
print(f'A soma dos {quant} nº é {soma} e sua media é {media}')

'''----------------------------------------------------------------------------'''
# 5 - GERA 2 Nº INTEIROS E FALA OS Nº INTEIROS ENTRE OS 2 PRIMEIROS
a = input('Diga o primeiro numero: ')
while not a.isnumeric():
    n = input('Diga o numero: ')
a = int(a)

b = input('Diga o primeiro numero: ')
while not b.isnumeric():
    b = input('Diga o numero: ')
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a, end='')
    a += 1

'''----------------------------------------------------------------------------'''
# 6 - VALIDANDO NOME DE USUARIO E SENHA
nU = input('Qual seu nome de usuario? ')
senha = input('Qual a sua senha? ')
while nU == senha:
    print('Acesso Negado,pq a senha não pode ser igual ao usuario! ')
    nU = input('Qual seu nome de usuario? ')
    senha = input('Qual a sua senha? ')
print('Acesso Permitido! ')

'''----------------------------------------------------------------------------'''
# 7 - SENHA E TENTATIVAS
senha = '1234'
senha_tentativas = input('Diga a senha: ')
tent = 1
while senha != senha_tentativas and tent < 3:
    print(f'Vc é hacker? Só mais {3 - tent} tentativas')
    senha_tentativas = input('Diga a senha: ')
    tent += 1
if senha == senha_tentativas:
    print('Acesso cadastrado! ')
else:
    print('Sai hacker')

'''----------------------------------------------------------------------------'''
# 8 - TABUADA
n = int(input('Diga um valor para tabuada: '))
print('{} X {} = {}'.format(n, 1, n * 1))
print('{} X {} = {}'.format(n, 2, n * 2))
print('{} X {} = {}'.format(n, 3, n * 3))
print('{} X {} = {}'.format(n, 4, n * 4))
print('{} X {} = {}'.format(n, 5, n * 5))
print('{} X {} = {}'.format(n, 6, n * 6))
print('{} X {} = {}'.format(n, 7, n * 7))
print('{} X {} = {}'.format(n, 8, n * 8))
print('{} X {} = {}'.format(n, 9, n * 9))
print('{} X {} = {}'.format(n, 10, n * 10))

'''----------------------------------------------------------------------------'''
# 8 - CORREÇÃO
n = input('Diga um valor ´para tabuada: ')
while not n.isnumeric():
    n = input('Diga um valor ´para tabuada: ')
n = int(n)
mult = 1
while n <= 10:
    while mult <= 10:
        print(f'{n} x {mult} = {n*mult}')
        mult += 1
        break

#         OU

n = 1
while n <= 10:
    print(f'Tabuada do {n} ')
    mult = 1
    while mult <= 10:
        print(f'{n} x {mult} = {n * mult}')
        mult += 1
    print()
    n += 1


'''----------------------------------------------------------------------------'''
# 9 - SEQUENCIA DE FIBONACCI
n = input('Quantos termos vc quer mostrar: ')
while not n.isnumeric():
    n = input('Quantos termos vc quer mostrar: ')
n = int(n)
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')

'''----------------------------------------------------------------------------'''
# 10 - PEDIR 10 Nº INTEIROS E VER QUANTOS SÃO PARES E QUANTOS SÃO ÍMPARES
cont = 0
par = 0
impar = 0
while cont < 10:
    n = input(f'Diga o {cont + 1}º numero: ')
    while not n.isnumeric():
        n = input(f'Diga o {cont + 1}º numero: ')
    n = int(n)
    cont += 1
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Dos 10 nº, foram digitados {par} numeros pares e {impar} impares')

'''----------------------------------------------------------------------------'''
# 11 - FATORIAL
from math import factorial
n = input('Diga o numero para calcular o fatorial: ')
while not n.isnumeric():
    n = input('Diga o numero para calcular o fatorial')
n = int(n)
f = 1
print(f'Fatorial de {n}! = ', end='')
while n > 0:
    print(f'{n}', end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f'{f}')

'''----------------------------------------------------------------------------'''
# 12 - VER SE O Nº É PRIMO OU N
num = input('Diga um numero: ')
while not num.isnumeric():
    num = input('Diga um numero: ')
num = int(num)
cont = 2
while cont < num:
    print(f'{num} % {cont} = {num%cont}')
    if num % cont == 0:
        print('Não é primo ')
        break
    elif cont == num - 1:
        print('É primo ')
    cont += 1

'''----------------------------------------------------------------------------'''
# 13 - MEDIA DE N NOTAS
quant = input('Quantas notas vc deseja calcular: ')
while not quant.isnumeric():
    quant = input('Quantas notas vc deseja calcular: ')
quant = int(quant)
soma = 0
cont = 0
while cont < quant:
    nota = input('Diga sua nota: ')
    while not nota.isnumeric():
        nota = input('Diga a sua nota: ')
    nota = int(nota)
    soma += nota
    cont += 1
media = soma / quant
print(f'A media entre as notas é {media:.2f}')

'''----------------------------------------------------------------------------'''
# 14 - SALARIO DE UM FUNCIONARIO A CADA ANO COM AUMENTO
salario = 1000
ano = 1995
taxa_inicial = 0.015
while ano < 2000:
    taxa = 1 + taxa_inicial
    taxa_inicial *= 2
    salario *= taxa
    ano += 1
print(f'{salario:.2f}')

'''----------------------------------------------------------------------------'''
# 15 - Nº POSITIVOS E QUAIS ESTÃO NESSES INTERVALOS:[0-25] - [26-50] - [51-75] - [76-100]
intervalo_1 = intervalo_2 = intervalo_3 = intervalo_4 = 0
while True:
    num = input('Diga um numero: ')
    while not num.isnumeric():
        print('Invalido! ')
        num = input('Diga um numero: ')
    num = int(num)
    if num < 25:
        intervalo_1 += 1
    elif num < 50:
        intervalo_2 += 1
    elif num < 75:
        intervalo_3 += 1
    elif num < 100:
        intervalo_4 += 1
    else:
        print('Tem q ser entre 0 e 10 ')
    
    cont = input('Quer continuar [s/n]?\n-> ')
    while not cont == 's' or cont == 'n':
        cont = input('Quer continuar [s/n]?\n-> ')
    if cont == 'n':
        break

'''----------------------------------------------------------------------------'''
# 16 - VOTACAO
qnt_candidato_1 = qnt_candidato_2 = qnt_candidato_3 = qnt_candidato_4 = brancos = nulos = 0
while True:
    num = input('Diga \n1 - Joao,'
                '\n2 - Maria'
                '\n3 - Sebastiao'
                '\n4 - Lucas'
                '\n5 - Brancos'
                '\n6 - Nulos ')
    while not num.isnumeric():
        print('Invalido! ')
        num = input('Diga \n1 - Joao,'
                    '\n2 - Maria'
                    '\n3 - Sebastiao'
                    '\n4 - Lucas'
                    '\n5 - Brancos'
                    '\n6 - Nulos: ')
    num = int(num)
    if num == 1:
        qnt_candidato_1 += 1
    elif num == 2:
        qnt_candidato_2 += 1
    elif num == 3:
        qnt_candidato_3 += 1
    elif num == 4:
        qnt_candidato_4 += 1
    elif num == 5:
        brancos += 1
    else:
        nulos += 1
        
    proxima = input("Quer continuar? (s/n)\n->")
    while not (proxima == 's' or proxima == 'n'):
        proxima = input("Quer continuar? (s/n)\n->")
    if proxima == 'n':
        break
tot = qnt_candidato_1 + qnt_candidato_2 + qnt_candidato_3 + qnt_candidato_4
print(f'Joao - {qnt_candidato_1} votos'
      f'\nMaria - {qnt_candidato_2} votos'
      f'\nSebastiao - {qnt_candidato_3} votos'
      f'\nLucas - {qnt_candidato_4}'
      f'\nbrancos - {brancos}'
      f'\nNulos - {nulos}')
print(f'A porcentagem de votos nulos foi de {100*nulos/tot:.2f}')
print(f'A porcentagem de votos brancos foi de {100*brancos/tot:.2f}')
