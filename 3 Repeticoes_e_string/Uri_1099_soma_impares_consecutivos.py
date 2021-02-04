n = int(input())
soma = 0

for i in range(1, n+1):
    num = input().split()
    x = int(num[0])
    y = int(num[1])

    for linha in range(x+1, y):
        if linha % 2 == 1:
            soma += linha
    print(soma)


