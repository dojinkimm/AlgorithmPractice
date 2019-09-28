# BOJ 1781 - 컵라면
import sys

N = int(sys.stdin.readline())

problem = []
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    problem.append((x, y))
problem.sort()

ramen = []
deadline = 0
for p in problem:
    deadline = p[0]
    ramen.append(p[1])

    while deadline < len(ramen):
        ramen.remove(min(ramen))

print(sum(ramen))
