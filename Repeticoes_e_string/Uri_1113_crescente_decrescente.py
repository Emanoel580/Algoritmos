def main():
    x, y = input().split()
    x = int(x)
    y = int(y)

    while x != y:
        if y > x:
            print('Crescente')
        elif x > y:
            print('Decrescente')
        x, y = input().split()
        x = int(x)
        y = int(y)


main()
