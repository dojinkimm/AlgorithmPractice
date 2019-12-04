# BOJ 1654 - 랜선 자르기
import sys
r = sys.stdin.readline

K, N = map(int, r().split())
lan = [int(r()) for _ in range(K)]

answer = 0
left, right = 0, max(lan)

while left <= right:
    mid = (right+left+1)//2
    res = 0

    for l in lan:
        res += (l//mid)

    if res >= N:
        left = mid + 1
        if mid > answer:
            answer = mid
    else:
        right = mid - 1

print(answer)
