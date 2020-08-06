# Recebendo o valor de entrada
N = int(input())

# Tuple com os valores de notas padrão
notas = (100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00)

# Printando o valor de entrada
print(N)

for nota in notas:
    # Printando a saída formatada para a quantidade de cada nota
    print('%d nota(s) de' % (N/nota), 'R$ %s' % (str(nota).replace('.', ',0')))
    N = N % nota
