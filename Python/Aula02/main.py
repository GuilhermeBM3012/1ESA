frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Guilherme"
print(frase)

print('-------------------------------------')

frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("diga a quinta palavra: ")
print(frase)

print('-------------------------------------------------------')

#CALCULADORA INTELIGENTE

nome = input("Diga o seu nome: ")
print(f"Olá, {nome}! Bem vindo à calculadora inteligente! ")
a = int(input("Diga o primeiro número: "))
b = int(input("Diga o segundo número: "))
soma = a + b
sub = a - b
mult = a * b
div = a/b
pot = a ** b

print('Para somar [1] ')
print('Para subtrair [2] ')
print('Para multiplicar [3] ')
print('Para dividir [4] ')
print('Para potência [5] ')

escolha = int(input('Escolha uma opção: '))
print(f'Vc escolheu a opção {escolha}')

if escolha == 1:
    print('A soma entre {} e {} vale {}'.format(a, b, soma))
elif escolha == 2:
    print('A subtração entre {} e {} vale {}'.format(a, b, sub))
elif escolha == 3:
    print('A multiplicação entre {} e {} vale {}'.format(a, b, mult))
elif escolha == 4:
    print('A divisão entre {} e {} vale {}'.format(a, b, div))
elif escolha == 5:
    print('A potência entre {} e {} vale {}'.format(a, b, soma))
else:
    print('OPÇÃO ERRADA!!')

print('------------------------------------------------------------------------------')

#OR

a = 2
b = 3
print(f"O resultado de {a} > {b} or {a} < {b}, ou seja,{2 > 3} or {2 < 3} dá {2 > 3 or 3 > 2}")
print(f"O resultado de {a} != {b} or {a} <= {b}, ou seja,{2 != 3} or {2 <= 3} dá {2 != 3 or 3 >= 2}")
print(f"O resultado de {a} <= {b} or {a} >= {b}, ou seja,{2 <= 3} or {2 >= 3} dá {2 <= 3 or 3 >= 2}")
print(f"O resultado de {a} >= {b} or {a} > {b}, ou seja,{2 >= 3} or {2 > 3} dá {2 >= 3 or 3 > 2}")

print('----------------------------------------------------------------------------------------------------')

#VER SE PODE ESTACIONAR

idade = int(input("Diga a sua idade: "))
cartao = input('Vc tem o cartão de idoso ou deficiente [S/N - s/n]? ')
deficiente = input('Vc é deficiente [S/N - s/n]? ')

if idade >= 60 and cartao == 'S' or 's' and deficiente == 'N' or 'n':
    print('Vc não pode estacionar')
elif idade >= 60 and cartao == 'N' or 'n' and deficiente == 'S' or 's':
    print('Vc não pode estacionar')
elif idade < 60 and cartao == 'S' or 's' and deficiente == 'S' or 's':
    print('Vc não pode estacionar')
elif idade >= 60 and cartao == 'S' or 's' and deficiente == 'S' or 's':
    print('Vc pode estacionar')
elif idade >= 60 and cartao == 'S' or 's' and deficiente == 'N' or 'n':
    print('Vc não pode estacionar')
else: 
    print('OPÇÃO INVÁLIDA! LEIA E TENTE NOVAMENTE!!! ')
