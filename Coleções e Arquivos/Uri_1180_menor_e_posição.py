def main():
    n = input()
    numero = int(n)

    if 1 < numero < 1000:
        lista = list()

    n = input()
    numeros = n.split()

    for i in range(numero):
        lista.append(int(numeros[i]))

    menor = lista[0]
    posicao = 0
    for i in range(1, numero):
        if menor > lista[i]:
            menor = lista[i]
            posicao = i

    print(f'Menor valor: {menor}')
    print(f'Posicao:  {posicao}')


main()




