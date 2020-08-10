from math import sqrt, pow

inp = list(map(float, input().split(' ')))

a, b, c = inp

delta = pow(b, 2) - 4 * a * c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (- b + sqrt(delta)) / (2 * a)
    r2 = (- b - sqrt(delta)) / (2 * a)
    print('R1 = %.5f' % r1, 'R2 = %.5f' % r2, sep='\n')
