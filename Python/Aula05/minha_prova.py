# rm: 562114
# nome: Guilherme Barone Milani

print('Boas vindas!! ')
endereco = input('Informe seu endereço: ')
ano = int(input('Em que ano você nasceu? '))
idade = 2025 - ano


if idade > 18:
    print('-----------------------------------')
    print('OPÇÕES DE VINHO: ')
    print('Tinto ')
    print('Branco ')
    print('Especial ')
    print('-----------------------------------')
    opcao = input('Qual das tres opções você deseja? ')
    if opcao == 'Tinto':
        preco = 69.9
    elif opcao == 'Branco':
        preco = 45.99
    elif opcao == 'Especial':
        preco = 120
    else:
        print('Opção inválida! ')
    quantidade = int(input('Quantas garrafas você deseja? '))
    valor = preco * quantidade
    print(f'Você escolheu a opção {opcao} e {quantidade} garrafas ')
    if valor < 100:
        frete = 19.99
        final = frete + valor
        print(f'O valor final é R${final:.2f}')
    elif valor > 100:
        print('Parabéns você ganhou frete grátis ')
        final = valor
    print(f'O valor final é R${final:.2f}')
    print('-------------------------------------------')
    print('Informações finais: ')
    print(f'Obrigado pela compra. A mesma será enviada para {endereco}')
else:
    print('Não é permitida a venda para menores de 18 anos ')