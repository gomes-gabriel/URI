

def maior(a, b):
    return (a + b + abs(a - b))/2


inp = list(map(int, input().split()))
a, b, c = inp

print('%d eh o maior' % (maior(a, maior(b, c))))
