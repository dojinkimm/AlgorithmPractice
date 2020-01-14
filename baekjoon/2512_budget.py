# BOJ 2512 - 예산 - 이분 탐색
import sys
r = sys.stdin.readline


def in_limit(limit):
    summ = 0
    for b in budget:
        summ += min(b, limit)
    return summ

N = int(r())
budget = sorted(list(map(int, r().split())))
total = int(r())

lo = 0
hi = budget[N-1]
answer = 0
while lo <= hi:
    mid = (lo+hi)//2
    added = in_limit(mid)
    if added <= total:
        answer = mid
        lo = mid+1
    else:
        hi = mid-1
print(answer)


