valor_entrada = float(input())

notas = (100, 50, 20, 10, 5, 2)
moedas = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

print('NOTAS:')
for valor in notas:
    print(str(int(valor_entrada // valor)) + ' nota(s) de R$ %.2f' % valor)
    valor_entrada = valor_entrada % valor + 0.001

print('MOEDAS:')
for valor in moedas:
    print(str(int(valor_entrada // valor)) + ' moeda(s) de R$ %.2f' % valor)
    valor_entrada = valor_entrada % valor
