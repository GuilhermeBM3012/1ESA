ano = input('DIga o seu ano de nascimento: ')
while not ano.isnumeric():
    ano = input('DIga o seu ano de nascimento: ')
ano = int(ano)

vinho1 = 'Pérgola'
vinho2 = 'Sangue de boi'
vinho3 = 'Cantinho do vale'
preco1 = 10
preco2 = 30
preco3 = 50
qtd1 = qtd2 = qtd3 = 0
idade = 2025 - ano

if idade < 18:
    print('Q feio, vou contar para sua mãe! ')
else:
    endereco = input('Diga seu endereço: ')
    valorTot = 0
    while True:
        escolha = input(f'Essa são as nossas opções:\n{vinho1} - {preco1}'
                        f'\n{vinho2} - {preco2}'
                        f'\n{vinho3} - {preco3}'
                        '\nQual você quer?')
        while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
            print(f'{escolha} é uma opção inválida')
            escolha = input(f'Essa são as nossas opções:\n{vinho1} - {preco1}'
                            f'\n{vinho2} - {preco2}'
                            f'\n{vinho3} - {preco3}'
                            '\nQual você quer?')
        qtd = input(f'Quantas garrafas você deseja? ')
        while not qtd.isnumeric():
            qtd = input(f'Quantas garrafas você deseja? ')
        qtd = int(qtd)
        if escolha == vinho1:
            preco1 = preco1
            qtd1 += qtd
        elif qtd == vinho2:
            preco = preco2
            qtd2 += qtd
        else:
            preco = preco3
            qtd3 += qtd
        valorTot = preco * qtd
        continuar = input('Você quer continuar comprando [s/n]?\n->')
        while not(continuar == 's' or continuar == 'n'):
            continuar = input('Você quer continuar comprando [s/n]?\n->')
        if continuar == 'n':
            break

    frete = 10
    if valorTot >= 500:
        print('Frete Grátis!')
        frete = 0
    valorTot += frete
    print(f'Obrigado por comprar aqui. Você comprou: \n{qtd1} - {vinho1}'
          f'\n{qtd2} - {vinho2}'
          f'\n{qtd3} - {vinho3}')
    print(f'Totalizando: R${valorTot:.2f} e o pedido será enviado para {endereco}')