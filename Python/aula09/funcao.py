# REVISÃO

# FUNÇÕES

def verificaNum(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num

qtd = verificaNum('Quantos nº vc quer na lista: ')

lista = []
pares = impares = 0
for i in range(qtd):
    num = verificaNum(f'Diga o {i +1} nº: ')
    lista.append(num)

for i in range(qtd):
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'\nDa lista {lista}'
      f'\nTem {pares} nº pares e {impares} nº impares')

print('----------------------------------------------------------------')

def calculoLista(listaNum):
    soma = 0
    for num in listaNum:
        soma += num
    media = soma / len(listaNum)
    print(f'Da lista: {listaNum}, a soma é {soma} e a media é {media:.2f}')
    return soma, media


lista = [4, 1, 5, 7, 3, 6, 9, 2, 10, 8]
media = calculoLista(lista)
lista2 = [10, 2, 7, 4]
media = calculoLista(lista2)

print('----------------------------------------------------------------')

def verificaMior(listaNum):
    maiorIndice = listaNum[0]
    for i in range(len(listaNum)):
        if listaNum[i] > maiorIndice:
            maiorIndice = listaNum[i]
    print(f'O maior item da lista: {listaNum} é {maiorIndice}')
    return maiorIndice

lista = [22, 1, 7, 5, 8, 3, 5, 9, 1000, 11, 100, 232, 43, 23]
maior = verificaMior(lista)

print('----------------------------------------------------------------')

def obrigarVinhos(msg, listaVinhos):
    opcoes = '\n'.join(listaVinhos)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in listaVinhos:
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

lista = ['Pergola', 'Tinto', 'Rose']
escolha = obrigarVinhos('Qual vinho vc deseja?', lista)

sim_ou_nao = ['S', 'N']
continuar = obrigarVinhos('Vc deseja continuar comprando?\n->', sim_ou_nao)

print('----------------------------------------------------------------')

def precoCarros(listas, elem):
    for i in range(len(listas)):
        if lista[i] == elem:
            return i

def carros(msg, listaCarros, msg_erro = 'Erro'):
    opcoes = '\n'.join(listaCarros)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in listaCarros:
        print(msg_erro)
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

lista = ['Up', 'Gol', 'Uno', 'Polinho']
preco = [100, 2000, 50000, 1000000]
escolha = carros('Qual carro vc deseja?',lista)

indiceEscolha = precoCarros(lista, escolha)
print(f'Vc escolheu {escolha} e o seu preço é R${preco[indiceEscolha]:.2f}')

