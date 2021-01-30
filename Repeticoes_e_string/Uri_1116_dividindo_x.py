def main():
    n = int(input())

    for i in range(1, n+1):
        num = input().split()
        x = int(num[0])
        y = int(num[1])
        if x >= 0 and y > 0:
            divisao = x / y
            print('{:.1f}'.format(divisao))
        elif y == 0:
            print('divisao impossivel')
        else:
            divisao = x / y
            print('{:.1f}'.format(divisao))


main()
