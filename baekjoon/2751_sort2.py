# BOJ 2751 - 수 정렬하기 2
import sys
r = sys.stdin.readline
S = set()

for i in range(0, int(r())):
    S.add(int(r()))
for i in sorted(S):
    print(i)
