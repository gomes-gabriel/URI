# data input
inp = list(map(float, input().split()))

# data processing
A, B, C = inp
PI = 3.14159

# data output
print('TRIANGULO: %.3f' % (A * C/2))
print('CIRCULO: %.3f' % (PI * C**2))
print('TRAPEZIO: %.3f' % ((A + B) * C/2))
print('QUADRADO: %.3f' % (B ** 2))
print('RETANGULO: %.3f' % (A * B))
