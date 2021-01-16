def main():
    valores = input().split()
    n1, n2, n3, n4 = valores
    media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 4 + float(n4) * 1) / 10
    print('Media: {:.1f}'.format(media))
    if media >= 7.0:
        print('Aluno aprovado.')
    if media < 5.0:
        print('Aluno reprovado.')
    if 5.0 <= media <= 6.9:
        print('Aluno em exame.')
        y = float(input())
        print('Nota do exame: {}'.format(y))
        media2 = (y + media) / 2
        if media2 >= 5:
            print('Aluno aprovado.')
            print(f'Media final: {media2:.1f}')
        else:
            print('Aluno reprovado.')
            print(f'Media final: {media2:.1f}')

main()
