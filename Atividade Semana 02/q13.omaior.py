def main():
    valores = input().split()
    a = int(valores[0])
    b = int(valores[1])
    c = int(valores[2])

    maior = max(a, b, c)
    print('{} he o maior'.format(maior))


main()