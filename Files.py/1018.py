import locale

# Mudando a localização para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt-BR')

# Recebendo o valor de entrada
N = int(input())

# Tuple com os valores de notas padrão
notas = (100, 50, 20, 10, 5, 2, 1)

# Printando o valor de entrada
print(N)

for nota in notas:
    # Modificando a nota para o padrão brasileiro com R$
    nota_formatada = locale.currency(nota)

    # Printando a saída formatada para a quantidade de cada nota
    print('%d nota(s) de' % (N/nota), nota_formatada)
    N = N % nota
