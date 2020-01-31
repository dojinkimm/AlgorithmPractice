# BOJ 11403 - 경로 찾기 - BFS
import sys
from collections import deque

r = sys.stdin.readline

N = int(r())
arr = []
q = deque()
arr = [list(map(int, r().split())) for _ in range(N)]

answer = arr[:][:]
for i in range(N):
    visited = [False] * N
    for j in range(N):
        if arr[i][j] == 1:
            q.append([i, j])
            visited[j] = True

    while q:
        x, y = q.popleft()
        for k in range(N):
            if arr[y][k] == 1 and not visited[k]:
                visited[k] = True
                q.append([y,k])

    for k in range(N):
        if visited[k]:
            answer[i][k] = 1

for a in arr:
    print(" ".join(map(str, a)))
