inp = list(map(float, input().split(' ')))

N1, N2, N3, N4 = inp

avg = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print('Media: %.1f' % avg)

if avg >= 7.0:
    print('Aluno aprovado.')
elif avg < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')

    exame = float(input())
    print('Nota do exame: %.1f' % exame)

    avg = (avg + exame) / 2

    if avg >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % avg)
