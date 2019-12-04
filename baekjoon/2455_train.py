# BOJ 2455 - 지능형 기차
import sys

maxi, num = 0, 0
for _ in range(4):
    cout, cin = map(int, sys.stdin.readline().split())
    num += (cin-cout)
    maxi = max(maxi, num)

print(maxi)