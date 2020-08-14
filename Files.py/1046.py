inp = list(map(int, input().split()))

begin, end = inp

if begin == end:
    print('O JOGO DUROU 24 HORA(S)')
elif begin > end:
    print('O JOGO DUROU %d HORA(S)' % ((24 - begin) + end))
else:
    print('O JOGO DUROU %d HORA(S)' % (end - begin))
