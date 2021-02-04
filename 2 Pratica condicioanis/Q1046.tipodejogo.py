valores = input().split()
i, f = valores

i = int(valores[0])
f = int(valores[1])

if i < f:
    t = f - i
else:
    t = (24 - i) + f
print('O JOGO DUROU {} HORA(S)'.format(t))
