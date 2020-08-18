salary = float(input())

values = {400: 0.15, 800: 0.12, 1200: 0.10, 2000: 0.07}

if salary > 2000:
    print('Novo salario: %.2f' % (salary * 1.04))
    print('Reajuste ganho: %.2f' % (salary * 0.04))
    print("Em percentual: 4 %")
else:
    for value in values.keys():
        if salary <= value:
            print('Novo salario: %.2f' % (salary * (1 + values[value])))
            print('Reajuste ganho: %.2f' % (salary * values[value]))
            print(f"Em percentual: {'%d' % (values[value] * 100)} %")
            break
