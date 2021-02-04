def main():
    # Entrada
    a, b, c = [float(x) for x in input('lado: ').split(' ')]

    # processamento
    triangulo = area_triangulo(a, c)
    circulo = area_circulo(c)
    trapezio = area_trapezio(a, b, c)
    quadrado = area_quadrado(b)
    retangulo = area_retangulo(a, b)

    # saida
    print('TRIANGULO: {:.3f}'.format(triangulo))
    print('CIRCULO: {:.3f}'.format(circulo))
    print('TRAPEZIO: {:.3f}'.format(trapezio))
    print('QUADRADO: {:.3f}'.format(quadrado))
    print('RETANGULO: {:.3f}'.format(retangulo))


def area_triangulo(a, c):
    triangulo = a * c / 2
    return triangulo


def area_circulo(c):
    circulo = (c ** 2) * 3.14159
    return circulo


def area_trapezio(a, b, c):
    trapezio = (a + b) * (c / 2)
    return trapezio


def area_quadrado(b):
    quadrado = b ** 2
    return quadrado


def area_retangulo(a, b):
    retangulo = a * b
    return retangulo


main()
