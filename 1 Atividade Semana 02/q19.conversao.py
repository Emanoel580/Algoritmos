def main():
    n = int(input())
    
    h = n // 3600
    resto = n % 3600
    m = resto // 60
    s = resto % 60

    print('{}:{}:{}'.format(h, m, s))


main()


