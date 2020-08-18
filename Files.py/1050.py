import sys

inp = int(input())

DDDs = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro', 32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

for DDD in DDDs.keys():
    if DDD == inp:
        print(DDDs[DDD])
        sys.exit()

print('DDD nao cadastrado')
