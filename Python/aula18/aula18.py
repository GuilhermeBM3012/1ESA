def forca_opcao(msg, listaOpcoes):
    msg += '\n' + ' --- '.join(listaOpcoes) + '\n-->'
    opcoes = input(msg)
    if not opcoes in listaOpcoes:
        return forca_opcao(msg, listaOpcoes)
    return opcoes

def somar():
    try:
        num1 = float(input('Diga o 1º numero: '))
        num2 = float(input('Diga o 2º numero: '))
    except:
        print('Tem que ser um número! ')
        return None
    else:
        soma = num1 + num2
        return soma

def subtrair():
    try:
        num1 = float(input('Diga o 1º número: '))
        num2 = float(input('Diga o 2º número: '))
    except:
        print('Tem que ser um número! ')
        return None
    else:
        subtracao = num1 - num2
        return subtracao

def multiplicar():
    try:
        num1 = float(input('Diga o 1º número: '))
        num2 = float(input('Diga o 2º número: '))
    except:
        print('Tem que ser um número! ')
        return None
    else:
        multiplicacao = num1 * num2
        return multiplicacao

def dividir():
    try:
        num1 = float(input('Diga o 1º número: '))
        num2 = float(input('Diga o 2º número: '))
        divisao = num1 / num2
    except ZeroDivisionError:
        print('Não é possível dividir por zero !')
    except:
        print('Tem que ser um número! ')
        return None
    else:
        return divisao

def potencia():
    try:
        num1 = float(input('Diga a base: '))
        num2 = float(input('Diga o expoente: '))
    except:
        print('Tem que ser um número! ')
        return None
    else:
        pot = num1 ** num2
        return pot

def raizQuadrada():
    try:
        num1 = float(input('Diga o número: '))
    except:
        print('Tem que ser um número! ')
        return None
    else:
        raiz = num1 ** (1/2)
        return raiz

acoes = {
    'Somar': somar,
    'Subtrair': subtrair,
    'Multiplicar': multiplicar,
    'Dividir': dividir,
    'Potência': potencia,
    'Raiz quadrada': raizQuadrada
}

print('===== BEM VINDO À CALCULADORA INTELIGENTE =====')
while True:
    escolha = forca_opcao('Qual operação você deseja fazer? ', list(acoes.keys()))
    resultado = acoes[escolha]()

    print(f'\n✅ Resultado da operação "{escolha}": {resultado}\n')

    if forca_opcao('Você deseja realizar mais alguma outra operação? ', ['Sim', 'Não']) == 'Não':
        print('Calculos realizados com sucesso! Volte sempre 😊')
        break