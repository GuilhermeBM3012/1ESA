from operator import index

# 2 - TRAGA TODAS AS INFORMAÇÕES SOBRE UM CARRO DA SUA ESCOLHA
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

opcoes = ' --- '.join(carros['nomes'])
escolha = input(f'Qual desses carros vc quer?\n{opcoes}\n->')
while escolha not in carros['nomes']:
    escolha = input(f'Qual desses carros vc quer?\n{opcoes}\n->')
indice = carros['nomes'].index(escolha)
for key in carros.keys():
    print(f'{key}: {carros[key][indice]}')


# 3 - TRAGA TODAS AS INFORMAÇÕES SOBRE O CARRO MAIS CARO E O MAIS BARATO
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

print('O carro mais caro é:')
maisCaro = carros['preço'][0]
for p in carros['preço']:
    if p > maisCaro:
        maisCaro = p
indice = carros['preço'].index(maisCaro)
for key in carros.keys():
    print(f'{key}: {carros[key][indice]}')

print('\n----------------------'
      '\nO carro mais barato é:')
maisBarato = carros['preço'][0]
for p in carros['preço']:
    if p < maisBarato:
        maisBarato = p
indice = carros['preço'].index(maisBarato)
for key in carros.keys():
    print(f'{key}: {carros[key][indice]}')


# 5 - ADD UM NOVO CARRO
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}


# 6 - RETIRANDO UM CARRO DO DIC
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

opcoes = ' --- '.join(carros['nomes'])
escolha = input(f'Qual desses carros vc quer?\n{opcoes}\n->')
while escolha not in carros['nomes']:
    escolha = input(f'Qual desses carros vc quer?\n{opcoes}\n->')
indice = carros['nomes'].index(escolha)
for key in carros.keys():
    carros[key].pop(indice)
print(carros)

# 7 - TRAVA-LINGUA
frase = ('O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom '
         'desconstantinopolitanizador será.').lower().replace('.', '')
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
    texto = texto.replace(key, num[key]) # .replace(' ', '')
texto = texto.replace(' ', '')
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

for key in dic1.keys():
    if key in dic2:
        contadorIguais += 1
        listaIguais.append(key)
    else:
        contadorDiferente += 1
        listaDiferentes.append(key)

print(f'\nTemos {contadorIguais} chaves presentes em ambos os DICs, que são:'
      f'\n{listaIguais}')


for key in dic2.keys():
    if key not in dic1:
        contadorDiferente += 1
        listaDiferentes.append(key)

print(f'\nTemos {contadorDiferente} chaves que não sao comuns aos dois DICs, que são:'
      f'\n{listaDiferentes}')
