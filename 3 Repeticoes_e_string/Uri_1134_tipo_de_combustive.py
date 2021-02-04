def main():
    Alcool = 0
    Gasolina = 0
    Diesel = 0
    
    codigo = int(input())

    while codigo != 4:
        if codigo == 1:
            Alcool += 1
        elif codigo == 2:
            Gasolina += 1
        elif codigo == 3:
            Diesel += 1
            
        codigo = int(input())

    print('MUITO OBRIGADO')
    print(f'Alcool: {Alcool}')
    print(f'Gasolina: {Gasolina}')
    print(f'Diesel: {Diesel}')


main()