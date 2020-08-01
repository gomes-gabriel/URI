# data input 
inp1 = input().split()
inp2 = input().split()

# data processing
code1 = inp1[0]
num_code1 = int(inp1[1])
unit_value1 = float(inp1[2])

code2 = inp2[0]
num_code2 = int(inp2[1])
unit_value2 = float(inp2[2])

price = num_code1 * unit_value1 + num_code2 * unit_value2

# data output
print('VALOR A PAGAR: R$', '%.2f' % price)
