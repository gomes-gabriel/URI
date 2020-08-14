inp = list(map(int, input().split()))
before = inp.copy()
inp.sort()

for i in inp:
    print(i)
print()
for j in before:
    print(j)
