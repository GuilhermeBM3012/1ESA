def forca_opcao(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n->'
    opcoes = input(msg)
    while opcoes not in listaOpcoes:
        opcoes = input(msg)
    return opcoes

def acha_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def informacoes():
    escolha = forca_opcao('Diga qual carne vc quer: ', acougue['Carnes'])
    indice = acha_index(acougue['Carnes'], escolha)
    for key in acougue.keys():
        print(f'{key}: {acougue[key][indice]}')
    return

def adicionar():
    for key in acougue.keys():
        info = input(f'Diga o novo {key} ')
        acougue[key].append(info)
    print(acougue)
    return

def remover():
    escolha = forca_opcao('Diga qual carro vc quer excluir: ', acougue['Carnes'])
    indice = acha_index(acougue['Carnes'], escolha)
    for key in acougue.keys():
        acougue[key].pop(indice)
    print(acougue)
    return

def atualizar():
    atualizar = forca_opcao('Qual carne vc deseja atualizar', acougue['Carnes'])
    indice = acha_index(acougue['Carnes'], atualizar)
    for key in acougue.keys():
        acougue[key][indice] = input(f'Diga o novo {key} do {atualizar}:')
    return

acougue={
    'Carnes': ['Patinho', 'Picanha', 'Coxão Mole', 'Maminha', 'Fraldinha', 'Linguiça'],
    'R$/kg': [35.9, 80.00, 24.78, 50.00, 49.85, 15],
    'Estoque': [10, 50, 30, 15, 20, 100],
    'Validade': ['4', '7', '5', '9', '20', '50']
}
listaCrud = {
    1: '1- Mostrar informações',
    2: '2- Adicionar',
    3: '3- Remover',
    4: '4- Atualiuzar'
}

print(f'\n-----------------------------------'
      f'\n          MENU AÇOUGUE             '
      f'\n-----------------------------------')

while True:
    for v in listaCrud.values():
        print(f'{v}')

    escolha = input('Qual opção vc deseja?\n->')
    while not escolha.isnumeric():
        escolha = input('Qual opção vc deseja?\n->')
    escolha = int(escolha)
    
    while escolha not in listaCrud:
        print('Opção inválida. Escolha uma opção de 1 a 4!! ')
        escolha = input('Qual opção vc deseja?\n->')
    if escolha == 1:
        informacoes()
    elif escolha == 2:
        adicionar()
    elif escolha == 3:
        remover()
    else:
        atualizar()

    cont = input('Gostaria de continuar comprando? ').upper()
    while cont not in ('S', 'N'):
        cont = input('Gostaria de continuar comprando? ').upper()
    if cont == 'N':
        print('Obrigado pela visita!! :)')
        break
