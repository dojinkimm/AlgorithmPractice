# BOJ 11724 - 연결 요소의 개수 - DFS
import sys
r = sys.stdin.readline
sys.setrecursionlimit(5000)

def dfs(dot):
    visited[dot] = True
    for j in range(len(dots[dot])):
        next = dots[dot][j]
        if not visited[next]:
            dfs(next)


N, M = map(int, r().split())
dots = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int,r().split())
    dots[start].append(end)
    dots[end].append(start)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)