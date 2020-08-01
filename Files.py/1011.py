

def vol_esfera(raio):
    return 4/3 * PI * raio**3


PI = 3.14159
raio = float(input())

print('VOLUME = %.3f' % vol_esfera(raio))
