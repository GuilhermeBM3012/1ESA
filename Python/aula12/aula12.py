import random

# DICIONARIO

dic = {'chave':'valor'} #não permite repetição e a chave sempre será o da esquerda
print(dic['chave'])
print(dic['valor']) # da erro pq n tem nenhuma chave 'valor'

print('-------------------------------------------------------------------')

# ADD UMA NOVA CHAVE NOVA COM UM VALOR NOVO
dic['nova chave'] = 'novo valor'
print(dic)

# SUBSTITUI O VALOR DA CHAVE 'chave'
dic['chave'] = '123'
print(dic)

print('-------------------------------------------------------------------')

saudacoes={
    'oi':'ola',
    'tchau':'flw'
}

resposta = input("Diga oi ou tchau:")
if resposta == 'oi':
    print("Olá")
else:
    print('flw')

# ISSO É IGUAL A ISSO:
resposta = input("Diga oi ou tchau:")
print(saudacoes[resposta])

print('-------------------------------------------------------------------')

# ESCOLHE ALEATORIAMENTE UM ELEMENTO DA LISTA DA CHAVE DIGITADA
saudacoes={
    'oi':['ola','SALVE','iae','BÃO uai'],
    'tchau':['flw','tchau migo','bjssssss diva','até mais']
}

resposta = input("Diga oi ou tchau:")
print(random.choice(saudacoes[resposta]))

print('-------------------------------------------------------------------')

# FORMAS GEOMETRICAS
forma={
    '3':'Triângulo',
    '4':'Quadrado',
    '5':'Pentágono',
    '6':'Hexágono'
}

lados = input("Diga o número de lados:")
print(f"Você escolheu um {forma[lados]}.")

print('-------------------------------------------------------------------')

# TROCANDO A CHAVE PELO SEU VALOR EM UM TEXTO C/ EMOJIS
emojis={
    ':)': '😊' ,
    ':(': '😔' ,
    '<3': '❤️' ,
    ":|": '😑'
}

texto = 'Eu amo python <3'
for key in emojis.keys():
    texto = texto.replace(key,emojis[key])
print(texto)

print('-------------------------------------------------------------------')

# TROCANDO A CHAVE PELO SEU VALOR EM UM TEXTO C/ Nº
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

tel = input('Digite seu telefone, de forma extensa(exemplo: nove):')
for key in num.keys():
    tel = tel.replace(key, num[key])
tel = tel.replace(' ', '') # remove os espaços
print(f'O seu nº é: {tel}')

print('-------------------------------------------------------------------')

# RELACIONANDO DUAS CHAVES COM OS SEUS ELEMENTOS
dic ={
    'nome': ['danilo', 'bernardo', 'matheus', 'luigi', 'guilherme', 'leandro'],
    'idade': [20, 30, 12, 17, 18, 22]
}

for i in range(len(dic['nome'])):
    for key in dic.keys():  # passa por todas as chaves mostrando o conteudo daquela chave
        print(f'{key} : {dic[key][i]}')
    print()

print('-------------------------------------------------------------------')

# CONTANDO QNTS VEZES UMA PALAVRA APARECE EM UM TRAVA-LINGUA ---> BAG OF WORDS
frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
frase = frase.lower()
frase = frase.replace('.', '')
palavras = frase.split(' ') # separa de acordo com o espaço e coloca em uma lista (contrario do join)
print(palavras)
contador={}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 1
    else:
        contador[palavra] += 1
print(contador)
