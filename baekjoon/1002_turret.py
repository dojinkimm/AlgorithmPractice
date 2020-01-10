# BOJ 1002 - 터렛
import sys
r = sys.stdin.readline

T = int(r())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, r().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        dist = (pow(x2-x1, 2) + pow(y2-y1, 2)) ** 0.5
        # 두 점에서 만난다
        if abs(r1-r2) < dist < r1+r2:
            print(2)
        # 한 점에서 만난다
        elif abs(r1-r2) == dist or r1+r2 == dist:
            print(1)
        else:
            print(0)
