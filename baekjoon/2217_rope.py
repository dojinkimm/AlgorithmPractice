# BOJ 2217 - 로프 - Greedy
import sys
r = sys.stdin.readline

N = int(r())
max_w = [int(r()) for _ in range(N)]
ans = 0
for idx, w in enumerate(sorted(max_w, key=lambda x: -x)):
    weight = (idx + 1) * w
    if weight > ans:
        ans = weight
print(ans)

