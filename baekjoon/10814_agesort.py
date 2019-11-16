# BOJ 10814 - 나이순 정렬
import sys
r = sys.stdin.readline

N= int(r())
names = [list(map(str, r().split())) for _ in range(N)]
names.sort(key=lambda x: (int(x[0])))

for n in names:
    print(n[0], n[1])
