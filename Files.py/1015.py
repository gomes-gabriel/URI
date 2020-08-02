from math import sqrt, pow

p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))

distancia = sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2)) 

print('%.4f' % distancia)
