# BOJ 5585 - 거스름돈 - Greedy
import sys

N = 1000 - int(sys.stdin.readline())
change = [500, 100, 50, 10, 5, 1]
cnt = 0
for c in change:
    cnt += N//c
    N = N%c
    # if c <= N:
    #     minus = N//c
    #     cnt += minus
    #     N -= c*minus
print(cnt)