# BOJ 2667 - 단지번호붙히기
import sys
sys.setrecursionlimit(100000)
r = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, cnt):

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not visited[nx][ny] and zone[nx][ny] == '1':
            visited[nx][ny] = True
            cnt = dfs(nx, ny, cnt) + 1

    return cnt


N = int(r())
zone = [list(map(str, r().strip())) for _ in range(N)]
ans = []
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if zone[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            ans.append(dfs(i, j, 1))

print(len(ans))
for i in sorted(ans):
    print(i)

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000


# 7
# 0000100
# 0110101
# 1110101
# 0000111
# 0100000
# 0101110
# 0111000