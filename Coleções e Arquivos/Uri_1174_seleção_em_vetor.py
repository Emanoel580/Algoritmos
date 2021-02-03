def main():
    A = []
    for i in range(100):
        x = float(input())
        if x <= 10:
            A.append(x)
            print(f'A [{i}] = {x}')


main()
