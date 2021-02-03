def main():
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for tam in range(len(X)):
        X[tam] = int(input())
        if X[tam] <= 0:
            X[tam] = 1
        print(f'X[{tam}] = {X[tam]}')


main()
