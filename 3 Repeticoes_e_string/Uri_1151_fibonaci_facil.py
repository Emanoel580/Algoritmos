def main():
    n_termos = int(input())
    anterior = 0
    proximo = 0

    while(proximo < n_termos):
        print(proximo)
        proximo = proximo + anterior
        anterior = proximo - anterior

        if(proximo == 0):
            proximo = proximo + 1


main()