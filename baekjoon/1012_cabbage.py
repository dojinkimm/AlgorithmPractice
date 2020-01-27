# BOJ 1012 - 유기농 배추 - DFS
import sys
sys.setrecursionlimit(50000)
r = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, m, n):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if (0 <= nx < n) and (0 <= ny < m):
            if not visited[nx][ny] and arr[nx][ny] is 1:
                visited[nx][ny] = True
                dfs(nx, ny, m, n)


T = int(input())
for _ in range(T):
    M, N, K = map(int, r().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, r().split())
        arr[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 1:
                visited[i][j] = True
                dfs(i, j, M, N)
                cnt += 1
    print(cnt)
