# BOJ 6593 - 상범 빌딩
import sys
r = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [1, 0, -1]


def dfs(x, y, z, time, visit):

    for k in range(3):
        nz = z + dz[k]

        if 0 <= nz < L:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if (0 <= nx < R) and (0 <= ny < C) and not visit[nz][nx][ny] and build[nz][nx][ny] != '#':
                    visit[nz][nx][ny] = True
                    time = dfs(nx, ny, nz, time, visit) + 1

    return time


L, R, C = map(int, r().split())
S, E = [], []
build = []
for i in range(L):
    build.append([])
    for j in range(R+1):
        row = list(r().strip())
        if row:
            build[i].append(row)
            if 'S' in row:
                S = [i, j, row.index('S')]
            elif 'E' in row:
                E = [i, j, row.index('E')]


visited = [[[False]*C for _ in range(R)] for _ in range(L)]
answer = dfs(0, 0, 0, 0, visited)

if answer == -1:
    print("Trapped!")
else:
    print("Escaped in {} minute(s).".format(answer))

# 3 4 5
# S....
# .###.
# .##..
# ###.#
#
# #####
# #####
# ##.##
# ##...
#
# #####
# #####
# #.###
# ####E
#
# 1 3 3
# S##
# #E#
# ###
#
# 0 0 0