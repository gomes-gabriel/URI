N = int(input())

_hour = str(N // 3600)
N = N % 3600
_min = str(N // 60)
_sec = str(N % 60)

print(_hour + ':', _min + ':', _sec, sep='')
