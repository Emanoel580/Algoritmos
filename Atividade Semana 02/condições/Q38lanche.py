valores = input().split()

codigo = int(valores[0])
qtd_item = int(valores[1])
res = 0.0

if codigo == 1:
    res = 4.0 * qtd_item  
elif codigo == 2:
    res = 4.50 * qtd_item
elif codigo == 3:
    res = 5.0 * qtd_item
elif codigo == 4:
    res = 2.00 * qtd_item
elif codigo  == 5:
    res = 1.50 * qtd_item


print('Total: R$ {:.2f}'.format(res))
