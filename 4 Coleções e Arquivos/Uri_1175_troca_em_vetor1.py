def main():
    N = []
    for i in range(20):
        x = int(input())
        N.append(x)
    y = N[::-1]
    for tam in range(20):
        print('N[{}] = {}'.format(tam, y[tam]))


main()
