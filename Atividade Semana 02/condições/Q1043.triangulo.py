def main():
    valores = input().split()
    a, b, c = valores
    a = float(a)
    b = float(b)
    c = float(c)

    perimetro = a + b + c
    area = (a + b) * c / 2

    if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
        print(f'Perimetro = {perimetro:.1f}')
    else:
        print(f'Area = {area:.1f}')


main()


