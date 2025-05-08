vogais = 0
for nome in 'guilherme':
    if nome == 'a' or nome == 'e' or nome == 'i' or nome == 'o' or nome == 'u':
        vogais += 1

# -------------------------------------------------------------------------------
pares = 0
for i in range(11):  # 11 pq ele conta um a menos
    num = int(input('Diga um numero: '))
    if num % 2 == 0:
        pares += 1

# ------------------------------------------------------------------------------
for i in range(11):
    print(i)
    i = 0
    print(i)

# ------------------------------------------------------------------------------
for i in range(1, 10, 2):  # vai do 1 ao 10, pulando 2
    print(i)
    i = 0
    print(i)

# ------------------------------------------------------------------------------
for i in range(20, 0, -2):  # vai do 20 ao 0, pulando 2
    print(i)
    i = 0
    print(i)

