name = input()
salary = float(input())
sold = float(input())

new_salary = salary + sold * 0.15

print('TOTAL = R$', "%.2f" % new_salary)
