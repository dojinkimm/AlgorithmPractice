# BOJ 10827 - a^b
import sys

a, b = map(str, sys.stdin.readline().split())

pt = a.index('.')
below_zero = len(a[pt+1:])
answer = str(pow(int(a[:pt]+a[pt+1:]), int(b)))
below_zero *= int(b)
if len(answer) < below_zero:
    answer = '0.' + '0'*(below_zero - len(answer)) + answer
else:
    below_zero = len(answer) - below_zero
    answer = answer[:below_zero] + '.' + answer[below_zero:]
print(answer)