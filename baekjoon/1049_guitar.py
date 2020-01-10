# BOJ 1049 - 기타줄 - Greedy
import sys
r = sys.stdin.readline
INF = 1000

N, M = map(int, r().split())
cheap_pack, cheap_one = INF, INF
for _ in range(M):
    pack, one = map(int, r().split())
    cheap_pack = min(cheap_pack, pack)
    cheap_one = min(cheap_one, one)

price = 0
if N >= 6:
    if N % 6 == 0:
        price = min(cheap_pack * (N//6), cheap_one * N)
    else:
        price = min(cheap_pack * (N//6) + cheap_one * (N % 6), cheap_pack * (N//6 + 1))
        price = min(price, cheap_one * N)
else:
    price = min(cheap_pack, cheap_one*N)
print(price)
