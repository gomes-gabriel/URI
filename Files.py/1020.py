DAYS = int(input())

years = DAYS // 365
DAYS = DAYS % 365
month = DAYS // 30
days = DAYS % 30

print(str(years) + ' ano(s)', str(month) + ' mes(es)', 
str(days) + ' dia(s)', sep='\n')
