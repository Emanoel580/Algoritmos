def main():
    n = int(input('qtd de testes: '))

    for i in range(1, n + 1):
        valores = input().split()
        a, b, c = valores

        media_ponderada = (float(a) * 2 + float(b) * 3 + float(c) * 5) / 10

        print(f'{media_ponderada:.1f}')


main()
