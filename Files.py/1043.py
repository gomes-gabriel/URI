inp = list(map(float, input().split()))

a, b, c = inp

inp.sort()

if inp[0] + inp[1] > inp[2]:
    print('Perimetro = %.1f' % (a + b + c))
else:
    print('Area = %.1f' % ((a + b) * c / 2))
