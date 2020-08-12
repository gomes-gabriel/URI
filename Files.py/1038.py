inp = list(map(int, input().split(' ')))

cod, qtd = inp

dic = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

for chave in dic.keys():
    if chave == cod:
        print('Total: R$ %.2f' % (dic[cod] * qtd))
        break
