inter, gre = input().split()
inter = int(inter[0])
cont_inter = 0
gre = int(gre[1])
cont_gre = 0
empates = 0

rep = int(input())
qtd = 0
print('Novo grenal (1-sim 2-nao')
while rep == 1:
    if rep == 1:
        inter, gre = input().split()
        print('Novo grenal (1-sim 2-nao')
qtd += 1
print(f'{qtd}', 'grenais')
print(f'Inter {cont_inter}')
print(f'Gremio {cont_gre}')
if cont_inter == cont_gre:
    empates += 1
    print(f'Empates {empates}')
if cont_inter > cont_inter:
    print('Inter venceu mais')
elif cont_gre > cont_inter:
    print('Gremio venceu mais')
# ERRADO, ESTOU TENTANDO