inp = list(map(int, input().split()))

h1, min1, h2, min2 = inp

hours = h2 - h1
minutes = min2 - min1

if minutes < 0:
    minutes += 60
    hours -= 1
if hours < 0:
    hours += 24
if h1 == h2 and min1 == min2:
    hours = 24
    minutes = 0

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
