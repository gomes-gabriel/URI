inp = list(map(int, input().split()))

inp.sort()

if inp[1] % inp[0] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
