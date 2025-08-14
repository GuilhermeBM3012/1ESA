letra = (input('Diga uma letra do alfabeto: '))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra que vc escolheu: {letra} é uma vogal ')
else:
    print(f'A letra que vc escolheu: {letra} é uma consoante ')

print('---------------------------------------------------------------------------')

time = (input('Diga qual time vc torce: '))
if time == 'Palmeiras':
    print('Maior do Mundo')
elif time == 'São Paulo':
    print('Filho do Corinthians')
elif time == 'Corinthians':
    print('2005 foi roubado ')
elif time == 'Santos':
    print('Neymar e Pelé')

print('------------------------------------------------------------------------------')

s = float(input('Diga qual é o seu salário: '))

if s <= 1903:
    print('Nada será descontado ')
elif s <= 2826.65:
    p = 7.5
    taxa = (s * 7.5) / 100
    s = s - taxa
    print('Então a taxa de acordo com o seu salário é 7.5%. Vai ter que pagar R${:.2f} e o novo salário é R${:.2f}'.format(taxa, s))
elif s <= 3751.05:
    taxa = (s * 15) / 100
    s = s - taxa
    print('Então a taxa de acordo com o seu salário é 15%. Vai ter que pagar R${:.2f} e o novo salário é R${:.2f}'.format(taxa, s))

elif s <= 4664.68:
    taxa = (s * 22.5) / 100
    s = s - taxa
    print('Então a taxa de acordo com o seu salário é 22.5%. Vai ter que pagar R${:.2f} e o novo salário é R${:.2f}'.format(taxa, s))
else:
    taxa = (s * 27.5) / 100
    s = s - taxa
    print('Então a taxa de acordo com o seu salário é 7.5%. Vai ter que pagar R${:.2f} e o novo salário é R${:.2f}'.format(taxa, s))

print('---------------------------------------------------------------------------------')

s = float(input('Diga qual é o seu salário: '))
if s <= 1903:
    print('Nada será descontado!!')
elif s <= 2826.65:
    taxa = 7.5
elif s <= 3751.05:
    taxa = 15
elif s <= 4664.68:
    taxa = 22.5
else:
    taxa = 27.5
desconto = (s * taxa) / 100
s = s - desconto
print(f'Vc receberá R${s:.2f} após desconto de R${desconto:.2f}')

print('------------------------------------------------------------------')

# CALCULADORA INTELIGENTE
nome = input("Diga o seu nome: ")
print(f"Olá, {nome}! Bem vindo à calculadora inteligente! ")
entrar = input('Vc quer fazer contas? [S/N - s/n]')
a = int(input("Diga o primeiro número: "))
b = int(input("Diga o segundo número: "))
soma = a + b
sub = a - b
mult = a * b
div = a/b
pot = a ** b

opcao = input('Qual operação gostaria de fazer?\nsoma\nsubtração\nmultiplicação\ndivisão\npotência')
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


