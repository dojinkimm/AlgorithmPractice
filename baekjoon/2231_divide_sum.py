# BOJ 2231 - 분해합
import sys

N = int(sys.stdin.readline())

found = 0
for i in range(N):
    answer = digit = i
    while digit > 0:
        answer += (digit % 10)
        digit //= 10

    if answer == N:
        found = i
        break

print(found)
