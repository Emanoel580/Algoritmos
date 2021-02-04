def main():
    valores = int(input())
    num = 0

    for i in range(1, 100):
        x = int(input())
        if x > num:
            maior = x
            p = i + 1
            num = x

    print(maior)
    print(p)


main()
