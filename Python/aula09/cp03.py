# REVISAO DO CP03

def achar_indice(listas, elem):
    for i in range(len(listas)):
        if listas[i] == elem:
            return i

idade = input('Quantos anos vc tem?\n->')
while not idade.isnumeric():
    idade = input('Quantos anos vc tem?\n->')
idade = int(idade)

if idade < 17:
    print('Vc ainda n tem idade para comprar bebidas')
else:
    print('Bem vindo! :)')
    endereco = input('Diga o seu endereco: ')

    def vinhos(msg, listaVinhos):
        qtd1 = qtd2 = qtd3 = precoTotal = 0
        while True:
            opcoes = '\n'.join(listaVinhos)
            escolhas = input(f'{msg}\n{opcoes}\n->')
            while not escolhas in listaVinhos:
                escolhas = input(f'{msg}\n{opcoes}\n->')

            qntd = input('Quantas garrafas vc quer: ')
            while not qntd.isnumeric():
                qntd = input('Quantas garrafas vc quer: ')
            qntd = int(qntd)

            indice = achar_indice(listaVinhos, escolhas)
            if indice == 0:
                qtd1 += qntd
            elif indice == 1:
                qtd2 += qntd
            else:
                qtd3 += qntd

            precoTotal += qntd * precos[indice]

            cont = input('Vc deseja continuar comprando?\n->')
            while not cont in ('S', 'N'):
                cont = input('Vc deseja continuar comprando?\n->')
            if cont == 'N':
                break
        frete = 20
        if precoTotal >= 400:
            print('Frete grátis')
            frete = 0
            precoTotal += frete
        precoTotal += frete
        print(f'\nVc comprou'
                f'\n{qtd1} do {listaVinhos[0]}'
                f'\n{qtd2} do {listaVinhos[1]}'
                f'\n{qtd3} do {listaVinhos[2]}'
                f'\nTotalizando R${precoTotal:.2f} e seu pedido sera entregue em {endereco}')
        return qtd1, qtd2, qtd3

    lista = ['Tinto', 'Rose', 'Branco']
    precos = [100, 50, 250]
    escolha = vinhos('Qual vinho vc deseja?', lista)


print('-----------------------------------------------------------------------------------------------------------')
# MELHOR JEITO

def achar_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

idade = input('Quantos anos você tem?\n-> ')
while not idade.isnumeric():
    idade = input('Quantos anos você tem?\n-> ')
idade = int(idade)

if idade < 17:
    print('Você ainda não tem idade para comprar bebidas.')
else:
    print('Bem-vindo! :)')
    endereco = input('Diga o seu endereço: ')

    def escolher_opcao(msg, listaVinhos):
        opcoes = '\n'.join(listaVinhos)
        escolha = input(f'{msg}\n{opcoes}\n-> ').strip().title()
        while escolha not in listaVinhos:
            escolha = input(f'Opção inválida. {msg}\n{opcoes}\n-> ').strip().title()
        return escolha

    lista = ['Tinto', 'Rose', 'Branco']
    precos = [100, 50, 250]

    qtd1 = qtd2 = qtd3 = precoTotal = 0
    while True:
        escolha = escolher_opcao('Qual vinho você deseja?', lista)

        qntd = input('Quantas garrafas você quer? ')
        while not qntd.isnumeric():
            qntd = input('Quantas garrafas você quer? ')
        qntd = int(qntd)

        indice = achar_indice(lista, escolha)
        if indice == 0:
            qtd1 += qntd
        elif indice == 1:
            qtd2 += qntd
        else:
            qtd3 += qntd

        precoTotal += qntd * precos[indice]

        continuar = escolher_opcao('Você deseja continuar comprando?', ['S', 'N']).upper()
        if continuar == 'N':
            break

    frete = 20
    if precoTotal >= 400:
        print('Frete grátis!')
        frete = 0

    precoTotal += frete

    print(f'\nVocê comprou:')
    print(f'{qtd1} do {lista[0]}')
    print(f'{qtd2} do {lista[1]}')
    print(f'{qtd3} do {lista[2]}')
    print(f'Totalizando R${precoTotal:.2f} e seu pedido será entregue em {endereco}')
