def main():
    senha = int(input())
    while not senha == 2002:
        print('Senha Invalida')
        senha = int(input())
    print('Acesso Permitido')


main()
