# BOJ 2178 - 미로 찾기 - BFS
import sys
from collections import deque
r = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M = map(int, r().split())
arr = [list(r().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = deque()
q.append([0, 0, 1])
visited[0][0] = True

while q:
    x, y, cnt = q.popleft()

    if x == N-1 and y == M-1:
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and arr[nx][ny] == '1' and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append([nx, ny, cnt+1])
