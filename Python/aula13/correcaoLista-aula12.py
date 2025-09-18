def forca_opcao(msg, listaOpcoes):
    msg += '\n' + '\n'.join(listaOpcoes) + '\n->'
    opcoes = input(msg)
    while opcoes not in listaOpcoes:
        opcoes = input(msg)
    return opcoes

def acha_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def indiceMaior(lista):
    indiceMaior = 0
    for i in range(len(lista)):
        if lista[i] > lista[indiceMaior]:
            indiceMaior = i
    return indiceMaior

def indiceMenor(lista):
    indiceMenor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indiceMenor]:
            indiceMenor = i
    return indiceMenor


# 2 - TRAGA TODAS AS INFORMAÇÕES SOBRE UM CARRO DA SUA ESCOLHA
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}
def informacoes():
    escolha = forca_opcao('Diga qual carro vc quer: ', carros['nomes'])
    indice = acha_index(carros['nomes'], escolha)
    for key in carros.keys():
        print(f'{key}: {carros[key][indice]}')
    return


# 3 - TRAGA TODAS AS INFORMAÇÕES SOBRE O CARRO MAIS CARO E O MAIS BARATO
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}
def maiorMenor():
    maior = indiceMaior(carros['preço'])
    menor = indiceMenor(carros['preço'])
    print('\nO carro mais caro é: ')
    for key in carros.keys():
        print(f'{key}: {carros[key][maior]}')
    print('\n-------------------------'
          '\nO carro mais barato é: ')
    for key in carros.keys():
        print(f'{key}: {carros[key][menor]}')
    return


# 5 - ADD UM NOVO CARRO
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}
def adicionar():
    for key in carros.keys():
        info = input(f'Diga o novo {key} ')
        carros[key].append(info)
    print(carros)
    return


# 6 - RETIRANDO UM CARRO DO DIC
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}
def remover():
    escolha = forca_opcao('Diga qual carro vc quer excluir: ', carros['nomes'])
    indice = acha_index(carros['nomes'], escolha)
    for key in carros.keys():
        carros[key].pop(indice)
    print(carros)
    return

# ATUALIZANDO AS INFO DE UM CARRO
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}
def atualizar():
    atualizar = forca_opcao('Qual carro vc deseja atualizar', carros['nomes'])
    indice = acha_index(carros['nomes'], atualizar)
    for key in carros.keys():
        carros[key][indice] = input(f'Diga o novo {key} do {atualizar}:')
    return


# 7 - TRAVA-LINGUA
frase = ('O bispo de Constantinopla é um bom desconstantinopolitanizador. '
         'Quem o desconstantinopolitanizar, um bom '
         'desconstantinopolitanizador será.').lower()
for char in '.,:;?!':
    frase = frase.replace(char, '')

listaPalavras = frase.split(' ')

travaLingua={}
for palavra in listaPalavras:
    if palavra not in travaLingua.keys():
        travaLingua[palavra] = 1
    else:
        travaLingua[palavra] += 1
print(travaLingua)


# 8 - MUDAR Nºs EM EXTENSO PARA DIGITO
# VER COMO DEIXAR SO OS Nºs SEPARADOS
num={
    'zero': '0',
    'um': '1',
    'dois': '2',
    'três': '3',
    'quatro': '4',
    'cinco': '5',
    'seis': '6',
    'sete': '7',
    'oito': '8',
    'nove': '9'
}

texto = 'Eu tenho aula na sala nove zero três'
for key in num.keys():
    text = texto.replace(key+' ', num[key])
    texto = texto.replace(key, num[key])
print(texto)


# 9 / 10 - DIGA QUAIS CHAVES SAO IGUAIS E DIFERENTES ENTRE DOIS DICs
contadorIguais = contadorDiferente = 0

dic1 = {
    'marca': 'Nike',
    'modelo': 'Air Max',
    'cor': 'Preto',
    'tamanho': 42,
    'preço': 600
}

dic2 = {
    'marca': 'Adidas',
    'modelo': 'Ultraboost',
    'cor': 'Branco',
    'estoque': 15,
    'desconto': 10
}
listaIguais = []
listaDiferentes = []

for key1 in dic1.keys():
    if key1 in dic2:
        contadorIguais += 1
        listaIguais.append(key1)
    else:
        contadorDiferente += 1
        listaDiferentes.append(key1)

print(f'\nTemos {contadorIguais} chaves presentes em ambos os DICs, que são:'
      f'\n{listaIguais}')


for key2 in dic2.keys():
    if key2 not in dic1:
        contadorDiferente += 1
        listaDiferentes.append(key2)

print(f'\nTemos {contadorDiferente} chaves que não sao comuns aos dois DICs, que são:'
      f'\n{listaDiferentes}')