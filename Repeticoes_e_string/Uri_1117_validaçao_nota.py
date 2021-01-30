def main():
    inicio = 0
    med = 0

    while inicio < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            inicio = inicio + 1
            med = med + nota
        if nota < 0 or nota > 10:
            print('nota invalida')
    med = med / 2
    print('media = {:.2f}'.format(med))


main()
