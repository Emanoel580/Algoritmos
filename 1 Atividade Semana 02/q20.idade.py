def idade():
    dias = int(input())

    ano_dias = 365
    ano = dias // ano_dias
    resto = dias % ano_dias
    mes = resto // 30
    dia = resto % 30

    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(mes))
    print('{} dia(s)'.format(dia))


idade()

