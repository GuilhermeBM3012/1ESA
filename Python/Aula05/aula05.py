# É PAR OU ÍMPAR

i = 0
pares = 0
n = int(input(f'Diga o {i + 1}º valor: '))
if n % 2 == 0:
    pares += 1
i += 1

n = int(input(f'Diga o {i + 1}º valor: '))
if n % 2 == 0:
    pares += 1
i = i + 1

n = int(input(f'Diga o {i + 1}º valor: '))
if n % 2 == 0:
    pares += 1
i += 1

n = int(input(f'Diga o {i + 1}º valor: '))
if n % 2 == 0:
    pares += 1
i += 1

n = int(input(f'Diga o {i + 1}º valor: '))
if n % 2 == 0:
    pares += 1
i += 1

print(f'Você digitou {pares} números pares e {i - pares} números ímpares ! ')

#             SEGUNDA MANEIRA

i = 0
pares = 0
while n < 5:
    n = int(input(f'Diga o {i + 1}º valor: '))
    if n % 2 == 0:
        pares += 1
    i += 1
print(f'Você digitou {pares} números pares e {i - pares} números ímpares ! ')


# 3: VERIFICAÇÃO DE SENHA
senhacerta = '1234'
senha_fornecida = input('Diga uma senha: ')
tentativas = 1
while senha_fornecida != senhacerta and tentativas < 3:
    print(f'Vc errou! Somente {3-tentativas} tentativas restantes!!! ')
    senha_fornecida = input('Diga uma senha: ')
    tentativas = tentativas + 1
if senha_fornecida == senhacerta:
    print('Acesso Permitido!!! ')
else:
    print('Acesso Negado!!! ')


# OBRIGANDO O USUÁRIO A ESCREVER UM TEXTO QUE EU QUEIRA

s = str(input('Diga o seu sexo: '))
while s != 'masculino' and s != 'feminino':  # USA PQ TEM POUCAS OPÇÕES
    s = input('Diga masculino ou feminino: ')

#               COM O "OU"

s = str(input('Diga o seu sexo: '))
while not (s == 'masculino' or s == 'feminino'):  # USA PQ PODE SER Q TENHA 50 OPÇÕES (+ VIÁVEL)
    s = input('Diga masculino ou feminino: ')

# OBRIGANDO O USUÁRIO A ESCREVER UM NÚMERO QUE EU QUEIRA

num = input('Diga um número: ')
if num.isnumeric():
    num = int(num)
else:
    print('Vc não digitou um número!')
print(type(num))

#     OU

num = input('Diga um número: ')
while not num.isnumeric():
    print('Vc deve digitar um número! ')
    num = input('Diga um número: ')
num = int(num)

