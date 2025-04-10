print('Seja Bem vindo/a a vinharia Agnelo!! ')
ano = int(input('Diga o seu ano de nascimento: '))
idade = 2025 - ano
if idade < 18:
    print('Não é permitida a venda de bebidas para menor de 18 anos! ')
else:
    endereco = input('Diga seu endereço: ')
    vinho1 = 'Peróla'
    vinho2 = 'Sangue de boi'
    vinho3 = 'Cantinho do Vale'
    preco1 = 50
    preco2 = 30
    preco3 = 20
    escolha = input(f'Esses são os nossos vinhos: \n{vinho1} - {preco1}'
                    f'\n{vinho2} - {preco2}\n{vinho3} - {preco3}'
                    f'\nQual você quer?\n->')
    qtd = int(input(f'Quantas garrafas de {escolha} você quer?\n->'))
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3
    total = qtd * preco
    if total > 100:
        frete = 0
        print('Parabéns. Ganhou Frete Grátis')
    total = frete
    print(f'Obrigado por comprar conosco, você gastou R${total:.2f} e será entregue em {endereco}')
