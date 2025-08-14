# REVISAO DO CP03

idade = input('Quantos anos vc tem?\n->')
while not idade.isnumeric():
    idade = input('Quantos anos vc tem?\n->')
idade = int(idade)

if idade >= 18:
    print('Bem vindo! :)')
    endereco = input('Diga o seu endereco: ')
else:
    print('Vc ainda n tem idade para comprar bebidas')

def achar_indice(listas, elem):
    for i in range(len(listas)):
        if listas[i] == elem:
            return i

def vinhos(msg, listaVinhos):
    while True:
        qtd1 = qtd2 = qtd3 = 0
        opcoes = '\n'.join(listaVinhos)
        escolhas = input(f'{msg}\n{opcoes}\n->')
        while not escolhas in listaVinhos:
            escolhas = input('Qual vinho vc deseja: ')

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

        cont = input('Vc deseja continuar comprando?\n->')
        while not cont in 'SN':
            cont = input('Vc deseja continuar comprando?\n->')
        if cont == 'N':
            break

        precoTotal = qntd * precos[indice]
        print(f'\nVc comprou'
                f'{qtd1} do {listaVinhos[0]}'
                f'{qtd2} do {listaVinhos[1]}'
                f'{qtd3} do {listaVinhos[2]}'
                f'Totalizando R${precoTotal:.2f} e seu pedido sera entregue em {endereco}')

lista = ['Tinto', 'Rose', 'Branco']
precos = [100, 50, 250]
escolha = vinhos('Qual vinho vc deseja?', lista)
