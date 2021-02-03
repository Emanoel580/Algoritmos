def main():
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    v = int(input())
    for tam in range(len(n)):
        n[tam] = v
        v = v * 2
        print(f'N {tam} = {n[tam]}')


main()

