def main():
    tempo = int(input())
    vel = int(input())


    qtd_litros = tempo * vel / 12
    print('{:.3f}'.format(qtd_litros))


main()
