def main():
    valores = input().split()
    x, y = valores
    x = float(x)
    y = float(y)

    if x == 0:
        if y == 0:
            print('Origem')
        if y != 0:
            print('Eixo Y')
    if y == 0:
        if x != 0:
            print('Eixo X')
    if x > 0:
        if y > 0:
            print('Q1')
        if y < 0:
            print('Q4')
    if x < 0:
        if y > 0:
            print('Q2')
        if y < 0:
            print('Q3')


main()