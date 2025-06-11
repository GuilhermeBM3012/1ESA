#  Nº POSITIVOS E QUAIS ESTÃO NESSES INTERVALOS:[0-25] - [26-50] - [51-75] - [76-100]
def numeros (msg):
    int1 = int2 = int3 = int4 = 0
    while True:
        num = input(msg)
        while not num.isnumeric():
            print('Invalido! ')
            num = input(msg)
        num = int(num)
        if num < 25:
            int1 += 1
        elif num < 50:
            int2 += 1
        elif num < 75:
            int3 += 1
        elif num < 100:
            int4 += 1
        else:
            print('Tem q ser entre 0 e 100 ')

        cont = input('Quer continuar [S/N]? ').strip().upper()
        while cont not in ['S', 'N']:
            cont = input('Quer continuar [S/N]? ').strip().upper()
        if cont == 'N':
            break

    return int1, int2, int3, int4

n1, n2, n3, n4 = numeros('Diga o nº: ')
print(f'\nNa ordem: 1: {n1} nº'
        f'\n2: {n2} nº'
        f'\n3: {n3} nº'
        f'\n4: {n4} nº')


#-----------------------------------------------------------------------------------
# VOTAÇÃO
def votar(msg, listaOpcoes):
    c1 = c2 = c3 = c4 = c5 = c6 = 0
    while True:
        opcoes = '\n'.join(listaOpcoes)
        escolha = input(f'{msg}\n{opcoes}\n->')
        while escolha not in listaOpcoes:
            print('Invalido! ')
            escolha = input(f'{msg}\n{opcoes}\n->')

        if escolha == 'joao':
            c1 += 1
        elif escolha == 'maria':
            c2 += 1
        elif escolha== 'sebastiao':
            c3 += 1
        elif escolha == 'lucas':
            c4 += 1
        elif escolha == 'brancos':
            c5 += 1
        else:
            c6 += 1

        proxima = input("Quer continuar? (s/n)\n->")
        while not (proxima == 's' or proxima == 'n'):
            proxima = input("Quer continuar? (s/n)\n->")
        if proxima == 'n':
            break

    return c1, c2, c3, c4, c5, c6

lista = ['joao', 'maria', 'sebastiao', 'lucas', 'brancos', 'nulos']
v1, v2, v3, v4, v5, v6 = votar('Em quem vc quer votar: ', lista)

tot = v1 + v2 + v3 + v4 + v5 + v6
print(f'Joao - {v1} votos'
      f'\nMaria - {v2} votos'
      f'\nSebastiao - {v3} votos'
      f'\nLucas - {v4}'
      f'\nbrancos - {v5}'
      f'\nNulos - {v6}')
print(f'A porcentagem de votos nulos foi de {100 * v6 / tot:.2f}')
print(f'A porcentagem de votos brancos foi de {100 * v5 / tot:.2f}')


#-----------------------------------------------------------------------------------
# PEDIR 10 NUMEROS E ADD NA LISTA)
def nLista (msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    lista.append(num)

lista = []
for i in range(10):
    numero = nLista(f'Diga o {i + 1}º numero: ')
print(lista)


#-----------------------------------------------------------------------------------
# VENDO A POSÇÃO DO MAIOR Nº DA LISTA
def maior(listaOpcoes):
    indiceMaior = 0
    maior = listaOpcoes[indiceMaior]
    for i in range(len(listaOpcoes)):
        if listaOpcoes[i] > maior:
            maior = listaOpcoes[i]
            indiceMaior = i
    return indiceMaior

preco = [600, 50, 80, 1000000, 5]
carros = ['Mustang', 'Up', 'Gol', 'Polinho turbão manual', 'Uno']
indiceMaior = maior(preco)
print(f'O carro mais caro é o {carros[indiceMaior]}')


#-----------------------------------------------------------------------------------
# MOSTRA AS OPÇÕES DE CARROS:
def carro (msg, listaOpcoes):
    opcoes = '\n'.join(listaOpcoes)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while escolha not in listaOpcoes:
        print('Invalido! ')
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha

def acharIndice (lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = ['Mustang', 'Up', 'Gol', 'Polinho turbão manual', 'Uno']
preco = [600, 50, 80, 1000000, 5]

escolha = carro('Qual carro vc deseja?', carros)
indiceEscolha = acharIndice(carros, escolha)

print(f'O {escolha} custa R${preco[indiceEscolha]}')


#-----------------------------------------------------------------------------------
# CPs 1 E 2
def acharIndice (lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

ano = input('Diga o seu ano de nascimento: ')
while not ano.isnumeric():
    ano = input('DIga o seu ano de nascimento: ')
ano = int(ano)

idade = 2025 - ano
if idade < 18:
    print('Não podemos vender bebidas para menores! ')
else:
    endereco = input('Diga seu endereço:\n-> ')

    def pedido(msg, listaOpcoes):
        valorTot = 0
        qtd1 = qtd2 = qtd3 = 0

        while True:
            opcoes = '\n'.join(listaOpcoes)
            escolha = input(f'{msg}\n{opcoes}\n->')

            qtd = input("Quantas garrafas você deseja?\n->")
            while not qtd.isnumeric():
                qtd = input("Quantas garrafas você deseja?\n->")
            qtd = int(qtd)

            indice = acharIndice(listaOpcoes, escolha)
            if indice == 0:
                qtd1 += qtd
            elif indice == 1:
                qtd2 += qtd
            elif indice == 2:
                qtd3 += qtd
            else:
                print('Opção inválida.')

            valorTot += precos[indice] * qtd

            continuar = input('Você quer continuar comprando [s/n]?\n->')
            while not (continuar == 's' or continuar == 'n'):
                continuar = input('Você quer continuar comprando [s/n]?\n->')
            if continuar == 'n':
                break

        frete = 10
        if valorTot >= 500:
            print('Frete Grátis! ')
            frete = 0
            valorTot += frete
        valorTot += frete

        print(f'\nSua compra deu R${valorTot} e será enviada para {endereco} '
              f'\nObrigado pela compea :) !!! ')

        return qtd1, qtd2, qtd3

vinhos = ['Pérgola', 'Tinto', 'Rosé']
precos = [10, 30, 50]

v1, v2, v3 = pedido('Qual vinho vc deseja? ', vinhos)

